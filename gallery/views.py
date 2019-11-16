from django.shortcuts import render
from gallery.apps import S3BucketUtility

# Create your views here


def gallery(request):
    return render(request,
                  'gallery.html',
                  {'s3_images_array': S3BucketUtility().s3_images_array()},
                  )
