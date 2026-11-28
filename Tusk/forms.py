from django.forms import ModelForm
from django import forms
from .models import Tusks

class TuskForm(forms.ModelForm):
    class Meta :
        model = Tusks
        fields = ['title', 'target',  'importance']