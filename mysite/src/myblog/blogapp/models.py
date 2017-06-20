# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

#step 1
#step 1
#step 1
#step 1
#step 1
#models.py ma change gare pachi makemigrations garna parcha brah!!
class BlogPost(models.Model):
	"""blog ma chiane ciz haru cha yesma"""
	title = models.CharField(max_length = 120)
	content = models.TextField()
	created = models.DateTimeField()
	updated = models.DateTimeField()
	author = models.CharField(max_length = 120)
	publish = models.BooleanField(default =  False)
	
	def __str__(self):
		return self.title


class Comment(models.Model):
	name = models.CharField(max_length = 120)
	email = models.CharField(max_length = 120)
	content = models.TextField()

	def __str__(self):
		return self.content
	
class Testing(models.Model):
	"""test haneko"""
	title = models.CharField(max_length = 120)
	content = models.TextField
	tester = models.CharField(max_length =120)
	publish = models.BooleanField(default = False)

	def  __str__():
		return self.title
