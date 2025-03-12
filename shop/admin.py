from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from shop.models import Product, Category, Comment, Order
from users.models import CustomUser

admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active')
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_active')
    ordering = ('-id',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    filter_horizontal = ('groups', 'user_permissions')


class ProductInline(admin.StackedInline):
    model = Product


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ('id', 'title')


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


@admin.register(Product)
class ProductModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ['id', 'name', 'price', 'image_tag', 'my_order']
    search_fields = ('name', 'description')
    list_filter = ('updated_at', 'category')
    ordering = ('my_order',)

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'content', 'rating', 'product', 'is_private')
    search_fields = ('email', 'content', 'product__name')
    list_filter = ('rating', 'is_private')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'quantity', 'product')
    search_fields = ('full_name', 'phone', 'product__name')
    list_filter = ('created_at',)
