from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    model = CustomUser
    add_form = CustomUserCreationForm
    list_display = ('username', 'first_name', 'last_name')
    search_fields = ['username', 'first_name', 'last_name']
