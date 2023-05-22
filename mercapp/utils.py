import os
from werkzeug.utils import secure_filename
import boto3, botocore

from .models import Usertable, Product, Promotion, Category


def find_admin(login):
    admin = Usertable.query.filter_by(login=login).first()
    return admin


def get_all_products():
    products = Product.query.all()
    return products


def get_all_categories():
    categories = Category.query.all()
    return categories


def get_active_categories():
    categories = Category.query.filter(Category.title != "Aucune").all()
    return categories


def find_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    return product


def find_product_by_category(category):
    products = Product.query.filter_by(category=category).all()
    return products


def get_promotions():
    promotions = Promotion.query.all()
    return promotions


s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


def upload_file_to_s3(file, acl="public-read"):
    filename = secure_filename(file.filename)
    try:
        s3.upload_fileobj(
            file,
            os.getenv("AWS_BUCKET_NAME"),
            filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    # after upload file to s3 bucket, return filename of the uploaded file
    return filename
