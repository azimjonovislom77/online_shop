from django.contrib import admin
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.index, name='index'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products-of-category/<int:category_id>/', views.index, name='products_of_category'),
    path('product-create/', views.product_create, name='product_create'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/update/', views.update_product, name='update_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)