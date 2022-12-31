from django.contrib import admin
from django.urls import path, include
from home.views import *

admin.site.site_title = "Jawad Ahmed (Admin)"
admin.site.site_header = "Jawad Ahmed (Admin Panel)"
admin.site.index_title = "Welcome to Jawad Ahmed Webpage!"


urlpatterns = [
    path('', index, name='home'),
    path('about', AboutClass.as_view(), name='about'),
    path('contact/<int:id>', contact, name='contact'),
]
