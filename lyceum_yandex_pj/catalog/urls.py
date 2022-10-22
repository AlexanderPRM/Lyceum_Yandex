# from django.urls import include
from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.item_list),
    re_path(r'(?P<pk>\d+)/$', views.item_detail, name='details')
]
