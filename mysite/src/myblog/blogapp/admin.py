# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#step 2
#step 2
#step 2
#step 2
#step 2
#step 2

from .models import BlogPost, Comment, Testing

#admin ko page ma display garne stuff haru, optional IMO
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['id','title','author','created','publish']
	list_filter = ['updated','author','publish']
	search_fields = ['title','content']
	list_editable = ['publish']
	list_display_links = ['title','created']
	list_per_page = 3


class CommentAdmin(admin.ModelAdmin):
	list_display = ['id','name', 'email', 'content']
	list_per_page = 4
	search_fields = ['name']

class TestingAdmin(admin.ModelAdmin):
	list_display = ['title','content','tester','publish']
	list_per_page = 4
	search_fields = ['title','content']

# Register your models here.
#step 3
#step 3
#step 3
#step 3
#step 3

admin.site.register(BlogPost,BlogPostAdmin)

#duita lai mix garera pathako
#mix your shit here brah!!
#mixing
admin.site.register(Comment,CommentAdmin)
admin.site.register(Testing)