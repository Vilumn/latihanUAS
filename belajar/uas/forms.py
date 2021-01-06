from django.forms import ModelForm
from django import forms
from .models import *

class TambahBinatang(ModelForm):
    class Meta:
        model = Folder
        fields = '__all__'