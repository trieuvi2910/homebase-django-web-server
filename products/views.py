# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def products(request):
    listProduct = Product.objects.all()
    return render(request, 'products.html', {'listProduct': listProduct})

def product_detail(request, product_id):
    product = Product.objects.get(pk = product_id)
    return render(request, 'product_detail.html', {'product': product})