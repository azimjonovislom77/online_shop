from django.contrib import admin
from django.utils.html import format_html
from shop.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'price', 'category', 'display_image')
    search_fields = ('name',)
    list_filter = ('category',)
    list_per_page = 20
    readonly_fields = ('updated_at',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="border-radius: 5px;"/>', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"
