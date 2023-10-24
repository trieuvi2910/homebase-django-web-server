# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse
import requests
import logging
logger = logging.getLogger('django')

# Create your views here.
def users(request):
    # Use the Python proxy to fetch user data from the Express API
    proxy_url = "http://127.0.0.1:5000/api/user/all"
    response = requests.get(proxy_url)
    
    if response.status_code == 200:
        data = response.json().get('data')
        return render(request, 'users.html', {'listUser': data})
    else:
       return render(request, 'users.html', {'listUser': []})