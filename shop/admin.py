from django.contrib import admin

from shop.models import Product, Category, Comment

# Register your models here.


admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'created_at')
