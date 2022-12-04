from django.urls import path, re_path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    re_path(
        r'(?P<pk>[1-9]\d*)/$',
        views.ItemDetail.as_view(),
        name='item_detail'
        )
]
