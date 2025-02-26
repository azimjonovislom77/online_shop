from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='index'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
]
