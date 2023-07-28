from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import productImage
from django.contrib.auth.models import User
from .models import customUser, products


class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data["email"]

        if customUser.objects.filter(email=email).exists():
            raise forms.ValidationError("THIS ACCOUNT ALREADY EXISTS")

        return email

    class Meta:
        model = customUser
        fields = ["username", "first_name", "last_name", "email"]


class productForm(forms.ModelForm):
    class Meta:
        model = products
        exclude = ("user",)


class imageUploadForm(forms.ModelForm):
    class Meta:
        model = productImage
        fields = ["image"]
        exclude = ("product",)
