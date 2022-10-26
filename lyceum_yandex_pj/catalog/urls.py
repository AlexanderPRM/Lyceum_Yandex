# from django.urls import include
from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.item_list),
    re_path(r'^(?P<pk>[1-9][0-9]*)/$', views.item_detail)
]
