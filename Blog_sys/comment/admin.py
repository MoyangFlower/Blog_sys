from django.contrib import admin

from .models import Comment
from Blog_sys.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['nickname', 'target', 'create_time', 'content', 'email']
