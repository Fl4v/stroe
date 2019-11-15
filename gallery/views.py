from django.shortcuts import render
from gallery.apps import s3_image_url

# Create your views here.


def gallery(request):
    return render(request,
                  'gallery.html',
                  {'s3_images_url': s3_image_url()},
                  )
