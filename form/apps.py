from django.apps import AppConfig
from stroe.settings.base import s3_client


class FormConfig(AppConfig):
    name = 'form'


def upload_file_to_S3(file_to_upload, file_name):

    s3_folder = 'form_uploads/'
    s3_bucket = 'stroe-django-bucket'

    s3_client.upload_fileobj(file_to_upload, s3_bucket, s3_folder + file_name)
