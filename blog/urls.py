from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^games/$', views.post_list, name='post_list'),
    url(r'^game/(?P<pk>\d+)/comment/$', views.add_comment_to_game, name='add_comment_to_game'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
