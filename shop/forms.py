from django import forms

from shop.models import Product, Category, Comment, Order
from phonenumber_field.formfields import PhoneNumberField


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('product',)


class OrderModelForm(forms.ModelForm):
    phone = PhoneNumberField(region='UZ')

    class Meta:
        model = Order
        exclude = ('product',)
