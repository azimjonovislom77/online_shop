from django.contrib import admin
from shop.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "product", "created_at")
    search_fields = ("name", "text")


admin.site.register(Comment, CommentAdmin)
