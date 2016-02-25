from django.conf.urls import url
from . import views

app_name = 'profiles'
urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^post/img/$', views.post, name='post'),
    url(r'^post/text/$', views.postText, name='postText'),
    url(r'^threads/(?P<thread_name>.*)/$', views.thread, name='thread'),
]
