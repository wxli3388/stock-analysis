from django.urls import path

from . import views

urlpatterns = [
    path('ptt-stock-article', views.ptt_stock_article),
    path('stock-data', views.stock_data),
]