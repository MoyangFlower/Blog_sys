#  coding=utf-8
"""
Created:2019-09-22 14:00
@Author:Jacob Yang
function description: 
"""
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
	site_header = 'Blog_System'
	site_title = 'Blog_System管理后台'
	index_title = '首页'


custom_site = CustomSite(name='cus_admin')

