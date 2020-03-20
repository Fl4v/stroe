from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger
from gallery.apps import S3BucketUtility

# Create your views here


def gallery(request):

    page_gallery = Paginator(S3BucketUtility().s3_images_array(), 28)
    page = request.GET.get('page', 1)

    try:
        images = page_gallery.page(page)

    except PageNotAnInteger:
        images = page_gallery.page(1)

    return render(request,
                  'gallery.html',
                  {'s3_images': images},
                  )
