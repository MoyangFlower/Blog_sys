from django.shortcuts import render

from .models import Post, Tag


def post_list(request, category_id=None, tag_id=None):
	if tag_id:
		try:
			tag = Tag.objects.get(id=tag_id)
		except Tag.DoesNotExists:
			post = []
		else:
			post = tag.post_set.filter(status=Post.STATUS_NORMAL)
	else:
		post = Post.objects.filter(status=Post.STATUS_NORMAL)
		if category_id:
			post = post.filter(category_id=category_id)
	return render(request, 'blog/list.html', context={'post_list': post})


def post_detail(request, post_id=None):
	try:
		post = Post.objects.get(id=post_id)
	except Post.DoesNotExist:
		post = None
	return render(request, 'blog/detail.html', context={'post': post})
