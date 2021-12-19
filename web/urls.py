from django.contrib import admin
from django.urls import path, include

from web.views import HomePage

app_name = 'web'

urlpatterns = [
    path('', HomePage.as_view(), name='home')
]