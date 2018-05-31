from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^games/$', views.post_list, name='post_list'),
]
