from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('', views.FeedbackPage.as_view(), name='feedback'),
]
