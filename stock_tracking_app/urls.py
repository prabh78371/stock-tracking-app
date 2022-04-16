from django.contrib import admin
from django.urls import path
from .models import stock_tracking_model
from . import views

urlpatterns = [
    path('stockapi/',views.product_api,name="api"),
    path('stockapi/<int:id>',views.product_api,name="api"),
    path('productapi/',views.stock_api,name="product_api"),
    path('productapi/<int:id>',views.stock_api,name="product_api"),

]