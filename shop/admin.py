from django.contrib import admin
from django.utils.html import format_html
from shop.models import Product, Category

# Register your models here.


admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'id', 'category', 'price')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return 'No Image'

    image_tag.short_description = 'Image'
