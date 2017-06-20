from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = '__all__'

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'