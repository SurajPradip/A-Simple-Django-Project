from django.contrib import admin
from .models import customUser, productImage, products
from django.contrib.auth.admin import UserAdmin

admin.site.register(customUser, UserAdmin)
admin.site.register(products)
admin.site.register(productImage)
