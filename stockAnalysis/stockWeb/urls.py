from django.urls import path

from stockWeb import views

urlpatterns = [
    path('hi', views.index, name='index'),
]