from django.apps import AppConfig
import boto3
from os import environ

S3_BASE_URL = 'https://stroe-django-bucket.s3-eu-west-1.amazonaws.com/'

s3_client = boto3.client(
    's3',
    aws_access_key_id=environ['BOTO3_AWS_ACCESS_KEY'],
    aws_secret_access_key=environ['BOTO3_AWS_SECRECT_KEY'],
    region_name=environ['AWS_REGION'],
)


class GalleryConfig(AppConfig):
    name = 'gallery'


def s3_image_url():
    images_array = []

    bucket_content = s3_client.list_objects(
        Bucket='stroe-django-bucket')['Contents']

    for key in bucket_content:
        if key['Key'] != 'django_test/':
            images_array.append(S3_BASE_URL + key['Key'])

    return images_array
