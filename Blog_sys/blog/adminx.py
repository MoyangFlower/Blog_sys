from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Post, Category, Tag
from django.contrib.admin.models import LogEntry

from Blog_sys.base_admin import BaseOwnerAdmin
from .adminforms import PostAdminForm
from Blog_sys.custom_site import custom_site
from xadmin.layout import Row, Fieldset
from xadmin.filters import RelatedFieldListFilter, manager
import xadmin


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
	list_display = ('name', 'status', 'is_nav', 'create_time', 'post_count')
	form_layout = (
		Fieldset('name', 'status', 'is_nav'),
	)

	def post_count(self, obj):
		return obj.post_set.count()

	post_count.short_description = '文章数量'

	def save_models(self):
		self.new_obj.owner = self.request.user
		return super().save_models()


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
	list_display = ('name', 'status', 'create_time')
	form_layout = (
		Fieldset('name', 'status'),
	)

	def save_models(self):
		self.new_obj.owner = self.request.user
		return super().save_models()


class CategoryOwnerFilter(RelatedFieldListFilter):
	""" 自定义过滤器只展示当前用户分类"""
	@classmethod
	def test(cls, field, request, params, model, admin_view, field_path):
		return field.name == 'category'

	def __int__(self, field, request, params, model, model_admin, field_path):
		super().__init__(field, request, params, model, model_admin, field_path)
	# 重新获取lookup_choices  根据owner过滤
		self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
	form = PostAdminForm
	list_display = ['title', 'category', 'status', 'create_time', 'owner', 'operator']
	list_display_links = []
	list_filter = ['category']

	search_fields = ['title']

	actions_on_top = False
	actions_on_bottom = True

	save_on_top = False

	# 自定义文章页面布局
	form_layout = (
		Fieldset(
			'基础信息',
			Row('title', 'category'),
			'status',
			'tag'
		),
		Fieldset(
			'内容信息',
			'desc',
			'content',
		)
	)

	filter_horizontal = ('tag',)

	def operator(self, obj):
		return format_html(
			'<a href="{}">编辑</a>',
			# reverse('xadmin:blog_post_change', args=(obj.id,))
			self.model_admin_url('change', obj.id)
		)

	operator.short_description = '操作'

	# @property
	# def media(self):
	# 	css = {
	# 		'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css',),
	# 	}
	# 	js = ('',)
	# 	media = super().media
	# 	media.add_js(['https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'])
	# 	media.add_css({
	# 		'all': 'https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css',
	# 	})
	# 	return media


# @xadmin.sites.register(LogEntry)
# class LogEntryAdmin(object):
# 	list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']




