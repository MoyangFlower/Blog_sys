#  coding=utf-8
"""
Created:2019-09-22 13:13
@Author:Jacob Yang
function description: 
"""
from django import forms


class PostAdminForm(forms.ModelForm):
	desc = forms.CharField(widget=forms.Textarea, label='自定义摘要', required=False)
