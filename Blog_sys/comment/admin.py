from django.contrib import admin

from .models import Comment
from Blog_sys.custom_site import custom_site
from Blog_sys.base_admin import BaseOwnerAdmin


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['nickname', 'target', 'create_time', 'content', 'email']
