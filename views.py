from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

# To get one variable, tape app.config['MY_VARIABLE']

from .utils import Administrator

@app.route('/')
@app.route("/index/")
def index():
    title= "Notre catalogue de produits"
    image1= './static/temp/image_1_legumes.jpg'
    product1="Test1"
    category1="Cat1 de test"
    description1 = "This is a test"
    price1="50000€"
    return render_template("index.html",
                            title=title,
                            image1=image1,
                            product1 =product1,
                            category1 = category1,
                            description1 = description1,
                            price1 = price1
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
