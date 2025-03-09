from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from import_export import resources
from import_export.admin import ImportExportMixin
from shop.models import Product, Category, Comment

admin.site.unregister(Group)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    ordering = ('-id',)


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


@admin.register(Product)
class ProductModelAdmin(SortableAdminMixin, ImportExportMixin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ['id', 'name', 'price', 'image_tag', 'category', 'my_order']
    search_fields = ('name', 'description')
    list_filter = ('updated_at', 'category')
    ordering = ('my_order',)

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'rating', 'product', 'is_private')
    search_fields = ('full_name', 'email', 'product__name')
    list_filter = ('rating', 'is_private')
