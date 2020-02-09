from django.apps import AppConfig
from collections import defaultdict

from stroe.settings.base import S3_BUCKET, s3_client


class GalleryConfig(AppConfig):
    name = 'gallery'


class S3BucketUtility:

    def s3_images_dict(self):
        self.images_dict = defaultdict(list)

        bucket_content = s3_client.list_objects(
            Bucket='stroe-django-bucket')['Contents']

        for counter, key in enumerate(bucket_content[1:], start=5):
            self.images_dict[counter // 5].append(S3_BUCKET + key['Key'])

        return self.images_dict

    def s3_images_array(self):
        self.images_array = []

        bucket_content = s3_client.list_objects(
            Bucket='stroe-django-bucket', Marker='wedding_pictures/')['Contents']

        for key in bucket_content:
            self.images_array.append(S3_BUCKET + key['Key'])

        return self.images_array
