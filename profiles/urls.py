from django.conf.urls import url
from . import views

app_name = 'profiles'
urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^post/img/$', views.post, name='post'),
    url(r'^post/text/$', views.postText, name='postText'),
    url(r'^threads/(?P<thread_name>.*)/$', views.thread, name='thread'),
    url(r'^registerUser/$', views.registerUser, name='registerUser'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginUser/$', views.loginUser, name='loginUser'),
    url(r'^login/$', views.signin, name='signin'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
]
