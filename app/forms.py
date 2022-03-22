from django import forms
from .models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image','name','description', 'price', 'digital','author','year_published')