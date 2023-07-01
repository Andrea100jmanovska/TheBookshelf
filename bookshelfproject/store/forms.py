from django import forms
from .models import Product, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'zipcode', 'city',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'author', 'description', 'price', 'image', 'quantity', )
        widgets = {
            'category': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Category'
            }),
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Book Title'
            }),
            'author': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Book Author'
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Short Description'
            }),
            'price': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Price: 2357 = 23.57'
            }),
            'quantity': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Quantity'
            }),
            'image': forms.FileInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Click here to add image'
            }),
        }