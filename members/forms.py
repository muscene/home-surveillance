from django import forms
from .models import Members

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
