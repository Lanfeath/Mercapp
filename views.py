from flask import Flask, flash, render_template, request, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Login manager initialize
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

from .utils import get_all_products, find_admin
from .models import *


@app.route('/')
@app.route("/index/")
def index():
    product_database = get_all_products()

    return render_template("index.html",
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Notre catalogue de produits",
                           products=product_database,
                           )


@app.route('/viewproduct/', methods =["GET"])
@login_required
def addpromotion():

    message = request.args.get('message')

    product_database = get_all_products()

    return render_template("viewproduct.html",
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Ajouter une promotion",
                           products=product_database,
                           message=message,
                           )


@app.route('/addproduct/', methods=['GET', 'POST'])
@login_required
def addproduct():
    form = AddProductForm()
    message = ""

    if form.validate_on_submit():
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        price = request.form['price']
        picture = "d"
        unit = request.form['unit']
        promotion = 0

        # the data to be inserted into Product model - the table, product
        record = Product(title, description, price, picture, category, promotion, unit)

        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()

        # create a message to send to the template
        message = f"Les donnèes du nouveau produit {title} ont été insérées."
        return redirect(url_for("index", message=message))

    return render_template('addproduct.html',
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Ajouter un produit",
                           form=form)


@app.route('/promotion/', methods=['GET', 'POST'])
@login_required
def promotion():
    id_product = int(request.args.get("product_id")) - 1
    products = get_all_products()
    product = products[id_product]

    form = AddPromotiontForm()

    return render_template("viewproduct.html",
                           css_file=url_for('static', filename='css/custom.css'),
                           title="Ajouter une promotion",
                           product=product,
                           form=form,
                           )


@app.route('/login/', methods=['GET', 'POST'])
def login():
    message = ""

    # if user already logged in direct to viewproduct.html
    if current_user.is_authenticated:
        return redirect(url_for('viewproduct'))

    form = LoginForm()

    if form.validate_on_submit():
        user = find_admin(form.login.data)

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("viewproduct"))
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


if __name__ == "__main__":
    app.run()
