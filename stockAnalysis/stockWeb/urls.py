from django.urls import path

from stockWeb import views

urlpatterns = [
    path('ptt-stock-article', views.ptt_stock_article),
]