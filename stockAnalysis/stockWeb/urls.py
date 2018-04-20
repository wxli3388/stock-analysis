from django.urls import path

from stockWeb import views

urlpatterns = [
    path('', views.index, name='index'),
]