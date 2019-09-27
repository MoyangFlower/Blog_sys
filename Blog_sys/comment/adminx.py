from django.contrib import admin

from .models import Comment
from Blog_sys.custom_site import custom_site
from Blog_sys.base_admin import BaseOwnerAdmin
import xadmin


@xadmin.sites.register(Comment)
class CommentAdmin(object):
	list_display = ['nickname', 'target', 'create_time', 'content', 'email']
