from django.contrib import admin

from .models import Link, SideBar
from Blog_sys.custom_site import custom_site
from Blog_sys.base_admin import BaseOwnerAdmin


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
	list_display = ['title', 'href', 'weight', 'status', 'create_time', 'owner']
	fields = ['title', 'href', 'status', 'weight']

	def save_model(self, request, obj, form, change):
		obj.owner = request.user
		return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
	list_display = ['title', 'display_type', 'content', 'create_time', 'owner']
	fields = ['title', 'display_type', 'content']

	def save_model(self, request, obj, form, change):
		obj.owner = request.user
		return super(SideBarAdmin, self).save_model(request, obj, form, change)

