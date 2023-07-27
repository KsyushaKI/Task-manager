from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, label=_('First name'))
    last_name = forms.CharField(max_length=150, label=_('Last name'))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username')
