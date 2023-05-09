from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

# To get one variable, tape app.config['MY_VARIABLE']

from .utils import get_all_products


@app.route('/')
@app.route("/index/")
def index():
    products = [
        {
            'picture': '/static/temp/banane.jpg',
            'title': "Test1",
            'category': "Cat1 de test",
            'description': "This is a test",
            'price': "50000€",
            'promotion': "0",
        },
        {
            'picture': '/static/temp/parfum_hugo.jpg',
            'title': "Test2",
            'category': "Cat de test 2",
            'description': "This is a 2nd test",
            'price': "2*50000€",
            'promotion': "0.2",
        },
        {
            'picture': '../static/temp/poivrons.jpg',
            'title': "Test3",
            'category': "Cat de test 3e",
            'description': "This is Gioia",
            'price': "1000€",
            'promotion': "0.3",
        },
    ]

    product_database=get_all_products()

    return render_template("index.html",
                           title="Notre catalogue de produits",
                           products=product_database,
                           )


@app.route('/result/')
def result():
    gender = request.args.get('gender')
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    description = find_content(gender).description
    profile_pic = 'http://graph.facebook.com/' + uid + '/picture?redirect=false'
    # profile_pic = 'http://graph.facebook.com/me/picture?redirect=false'

    return render_template('result.html',
                           user_name=user_name,
                           user_image=profile_pic,
                           description=description,
                           blur=False)


if __name__ == "__main__":
    app.run()
