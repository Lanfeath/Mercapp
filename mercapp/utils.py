import os
from werkzeug.utils import secure_filename


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


# Config S3:
aws_bucket_name="mercappbin"
aws_access_key="AKIA4TJLCGSXLJYZOA4M"
aws_secret_access_key="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"

import boto3, botocore

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_access_key
)


def upload_file_to_s3(file, acl="public-read"):
    filename = secure_filename(file.filename)
    try:
        s3.upload_fileobj(
            file,
            aws_bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    # after upload file to s3 bucket, return filename of the uploaded file
    return file.filename