from django.urls import re_path as url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
]