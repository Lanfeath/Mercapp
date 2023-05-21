from flask import Flask, flash, render_template, request, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from datetime import datetime
import os
import uuid

app = Flask(__name__)

# Login manager initialize
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

from .utils import *
from .models import *


@app.route('/')
@app.route("/index/", methods=['GET', 'POST'])
def index():
    product_database = get_all_products()
    promotions = get_promotions()
    categories = get_all_categories()

    form = SelectCategory()
    form.categories.choices = [(category.title, category.title) for category in categories]

    if form.validate_on_submit():
        category = request.form['categories']
        if category == "Aucune":
            product_database = get_all_products()
        else:
            product_database = find_product_by_category(category)

    return render_template("index.html",
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Notre catalogue de produits",
                           products=product_database,
                           promotions=promotions,
                           categories=categories,
                           form=form,
                           )


@app.route('/addproduct/', methods=['GET', 'POST'])
@login_required
def addproduct():
    form = AddProductForm()
    form.category.choices = [(category.title, category.title) for category in get_active_categories()]

    if form.validate_on_submit():
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        price = request.form['price']
        unit = request.form['unit']
        promotion = None

        # Save picture in file config as UPLOAD
        f = form.picture.data
        picture_title = str(uuid.uuid4()) + ".jpg"
        f.save(os.path.join(app.config['UPLOAD'], picture_title))

        picture = url_for('static', filename='temp/') + picture_title

        # the data to be inserted into Product model - the table, product
        record = Product(title, description, price, picture, category, promotion, unit)

        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()

        # create a message to send to the template
        message = f"Les données du nouveau produit {title} ont été insérées."
        return redirect(url_for("index", message=message))

    return render_template('addproduct.html',
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Ajouter un produit",
                           form=form, )


@app.route('/promotion/', methods=['GET', 'POST'])
@login_required
def promotion():
    id_product = int(request.args.get("product_id") or 1)
    product = find_product(id_product)
    message = "no message"

    form = AddPromotiontForm()

    if form.validate_on_submit():
        percentage = request.form['percentage']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')

        # the data to be inserted into Promotion model - the table, promotion
        record = Promotion(start_date, end_date, percentage)

        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        # save change without commit
        db.session.flush()
        product.promotion = record.id
        db.session.commit()

        # create a message to send to the template
        message = f"Les donnèes du nouveau produit {product.title} ont été mises a jour."

    return render_template("addpromotion.html",
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Ajouter une promotion",
                           product=product,
                           form=form,
                           message=message,
                           )


@app.route('/login/', methods=['GET', 'POST'])
def login():
    message = ""

    # if user already logged in direct to index.html
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = find_admin(form.login.data)

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("index"))
            else:
                message = "mauvais mot de passe"
        else:
            message = "mauvais login"

    return render_template("login.html",
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Page de connection",
                           form=form,
                           message=message,
                           )


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/deleteproduct/', methods=["POST", "GET"])
def delete_product():
    id_product = int(request.args.get("product_id") or 1)
    product = find_product(id_product)
    message = "no message"

    if request.method == "POST":
        db.session.delete(product)
        db.session.commit()

        # create a message to send to the template
        message = f"Le produit {product.title} a été mises supprimé."
        return redirect(url_for("index", message=message))

    return render_template("deleteproduct.html",
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Supprimer un produit",
                           product=product,
                           message=message,
                           )


if __name__ == "__main__":
    app.run()
