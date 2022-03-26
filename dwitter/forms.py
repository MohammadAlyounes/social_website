from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Dweet, Profile


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class DweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
     widget=forms.widgets.Textarea(
        attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Dweet
        exclude = ("user", )


