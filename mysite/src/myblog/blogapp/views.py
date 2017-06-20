# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, CreateView

from .models import BlogPost,Comment
from .forms import BlogPostForm,CommentForm

# Create your views here.


#function based views ra class based views 
#function khasai use hunna!!

def home(request):
	"""asldkfj """
	template_name = 'blogapp/home.html'

	#views bata template ma stuff pathauna
	

	#importanter
	#importanter
	##importanter
	#####query set bata pathaune!! brah!!

	blogs = BlogPost.objects.all()
	context={'name':'Anuj Pokhrel','address':'pingalsthan','blogs':blogs}
	
	era={'python':'django','ruby':'rails','php':'laravel'}
	return render(request, template_name, context, era)

def contact(request):
	template = 'blogapp/contact.html'
	era={'python':'django','ruby':'rails','php':'laravel'}
	return render(request,template,era)

#templates bhanne folder banaune afno app bhitra

#class based views
class Ello(TemplateView):
	template_name = 'contact.html'

class Support(TemplateView):
	template_name ='support.html'


def create_blog(request):
	if request.method == "POST":
		blog = BlogPostForm(request.POST)
		if blog.is_valid():
			blog.save()
			return HttpResponse('YOur blog has been posted, Thank YOU')


	template_name = 'create_blog.html'
	context = {'form':BlogPostForm}
	return render(request, template_name,context)

def create_comment(request):
	if request.method == "POST":
		comment = CommentForm(request.POST)
		if comment.is_valid():
			comment.save()
			return HttpResponse("your comment has been recorded")

	template_name = 'create_comment.html'
	context = {'comment': CommentForm}
	return render(request, template_name,context)



class BlogList(ListView):
	model = BlogPost
	context_object_name = 'blogs'
	template_name = 'blog_list.html'


class CreateBlog(CreateView):
	model = BlogPost
	fields= '__all__'
	template_name = 'new_blog.html'
	success_url = '/'

class CreateComment(CreateView):
	model = Comment
	fields ='__all__'
	template_name = 'new_comment.html'
	success_url = '/'

class CommentList(ListView):
	model = Comment
	context_object_name = 'comment'
	template_name = 'comments.html'


#create view ra update view

def about(request):
	template_name =  'blogapp/about.html'
	return render(request,template_name)

def post(request):
	template_name = 'blogapp/post.html'
	return render(request,template_name)