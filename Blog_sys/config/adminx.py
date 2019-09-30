from django.contrib import admin
import xadmin

from .models import Link, SideBar
from xadmin.layout import Fieldset
from Blog_sys.base_admin import BaseOwnerAdmin


@xadmin.sites.register(Link)
class LinkAdmin(BaseOwnerAdmin):
	list_display = ['title', 'href', 'weight', 'status', 'create_time', 'owner']
	form_layout = (
		Fieldset('title', 'href', 'status', 'weight'),
	)

	def save_models(self):
		self.new_obj.owner = self.request.user
		return super().save_models()


@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
	list_display = ['title', 'display_type', 'content', 'create_time', 'owner']
	form_layout = (
		Fieldset('title', 'display_type', 'content'),
	)

	def save_models(self):
		self.new_obj.owner = self.request.user
		return super().save_models()

