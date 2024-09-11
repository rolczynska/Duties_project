from profiles.models import User
from django.contrib import admin


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'date_of_birth', 'phone_number')
    fields = ['username', 'email', 'first_name', 'last_name', 'role', 'date_of_birth', 'phone_number']


# Register your models here.
admin.site.register(User, CustomUserAdmin)
