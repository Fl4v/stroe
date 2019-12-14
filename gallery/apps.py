import boto3
from django.apps import AppConfig
from os import getenv
from collections import defaultdict

S3_BASE_URL = 'https://stroe-django-bucket.s3-eu-west-1.amazonaws.com/'


s3_client = boto3.client('s3', aws_access_key_id=getenv('BOTO3_AWS_ACCESS_KEY'),
                         aws_secret_access_key=getenv('BOTO3_AWS_SECRECT_KEY'),
                         region_name=getenv('AWS_REGION'),
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
