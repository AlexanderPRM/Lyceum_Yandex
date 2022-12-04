from django.urls import path

from about import views

app_name = 'about'

urlpatterns = [
    path('', views.AboutPage.as_view(), name='main')
]
