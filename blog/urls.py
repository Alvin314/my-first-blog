from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^posts/$', views.post_list, name='post_list'),
]
