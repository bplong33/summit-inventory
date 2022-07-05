from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import InventoryUser

# Register your models here.
admin.site.register(InventoryUser, UserAdmin)