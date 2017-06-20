from django.conf.urls import url


from .views import home,contact,Ello,Support,create_blog,create_comment,BlogList,CreateBlog,CreateComment,CommentList,about,post

urlpatterns = [url(r'^$',home,name= 'home'),
    url(r'^contact$',contact, name ='contact'),
    url(r'^list$',BlogList.as_view(), name='List'),
    url(r'^blog/new$',CreateBlog.as_view(), name= 'BlogNew'),
    url(r'^blog/comm$',CreateComment.as_view(), name= 'blog_comm_C' ),
    url(r'^comment$',CommentList.as_view(), name ='Comment'),
    url(r'^Ello$', Ello.as_view(), name='Ello'),
    url(r'^Support$', Support.as_view(), name='Support'),
 	url(r'^blog/create$', create_blog, name='blog_create'),
	url(r'^blog/comment$', create_comment, name = "blog_comment"),
	url(r'^about$',about, name='about'),
	url(r'^post$',post, name ='post'),

 ]