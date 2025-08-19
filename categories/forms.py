from django import forms
from .models import Category
from products.models import Product

class CategoryForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Category
        fields = ['name', 'description', 'image', 'products']
