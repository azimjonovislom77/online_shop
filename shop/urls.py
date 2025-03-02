from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('product/', views.index, name='index'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products-of-category/<int:category_id>/', views.index, name='products_of_category'),
    path('product-create/', views.product_create, name='product_create'),
    path('product-delete/<int:product_id>/', views.product_delete, name='product_delete'),
    path('product-update/<int:product_id>/', views.product_update, name='product_update'),
    path('product/<int:product_id>/add-comment/', views.add_comment, name='add_comment'),
    path('product/<int:product_id>/comments/', views.comment_list_view, name='comment_list'),
]
