# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post

def post_home(request):
	queryset = Post.objects.all()
	content = {
		"object_all": queryset,
		#"title": "List"
	}
	return render(request, "index.html",content)
