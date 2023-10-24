# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    list_filter = ('name', 'price')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)