from django import forms
from django.core.files.storage import default_storage

class PhotoForm(forms.Form):
    image=forms.ImageField(widget=forms.FileInput(attrs={"class":"custom-file-input"}))
