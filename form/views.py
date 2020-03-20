from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import UploadWeddingMedia
from .apps import upload_file_to_S3


def form(request):

    if request.method == 'POST':

        form = UploadWeddingMedia(request.POST, request.FILES)

        if form.is_valid():
            uploaded_files = request.FILES['media']

            upload_file_to_S3(uploaded_files, uploaded_files.name)

            return HttpResponseRedirect('/thank_you')

    else:
        form = UploadWeddingMedia()

    return render(request, 'form.html', {
        'form': form
    })
