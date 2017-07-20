# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "__unicode__", "timestamp"]
	list_display_links = ["updated"]
	list_filter = ["updated", "timestamp"]
	list_editable = ["title"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)



