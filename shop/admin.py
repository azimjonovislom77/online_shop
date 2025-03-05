from django.contrib import admin

from shop.models import Product, Category, Comment, Order

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'product', 'created_at')
    search_fields = ('full_name', 'phone', 'product__name')
    list_filter = ('created_at',)