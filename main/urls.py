from django.urls import path, include
from django.urls import re_path as url
from . import views

urlpatterns = [
path('', views.home, name = "Home"),
url(r'^main', views.product_list, name='product_list'),
url(r'^(?P<category_slug>[-\w]+)/main',
        views.product_list,
        name='product_list_by_category'),
url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/main',
        views.product_detail,
        name='product_detail'),
]