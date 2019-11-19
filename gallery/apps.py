from django.apps import AppConfig
from os import environ
from collections import defaultdict

from stroe.settings import S3_BASE_URL

import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id=environ['BOTO3_AWS_ACCESS_KEY'],
    aws_secret_access_key=environ['BOTO3_AWS_SECRECT_KEY'],
    region_name=environ['AWS_REGION'],
)


class GalleryConfig(AppConfig):
    name = 'gallery'


class S3BucketUtility:

    def s3_images_dict(self):
        self.images_dict = defaultdict(list)

        bucket_content = s3_client.list_objects(
            Bucket='stroe-django-bucket')['Contents']

        for counter, key in enumerate(bucket_content[1:], start=5):
            self.images_dict[counter // 5].append(S3_BASE_URL + key['Key'])

        return self.images_dict

    def s3_images_array(self):
        self.images_array = []

        bucket_content = s3_client.list_objects(
            Bucket='stroe-django-bucket')['Contents']

        for key in bucket_content[1:]:
            self.images_array.append(S3_BASE_URL + key['Key'])

        return self.images_array
