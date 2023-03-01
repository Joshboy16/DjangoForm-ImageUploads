from django import forms
from django.forms import ModelForm
from .models import Movie

class UploadForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()
    class Meta:
        model = Movie
        fields = ['name', 'image']