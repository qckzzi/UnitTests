from django.contrib import admin
from .models import *


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'secondname', 'user')


class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'vin')


admin.site.register(Car, CarsAdmin)

# Register your models here.
