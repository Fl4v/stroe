from django import forms


class UploadWeddingMedia(forms.Form):

    name = forms.CharField(max_length=20, required=True)
    media = forms.FileField(required=False)
