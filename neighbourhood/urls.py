from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     url(r'^house/(?P<id>[0-9]+)$',views.house, name='House'),
    url(r'^room/(?P<id>[0-9]+)$',views.room, name='Room'),
    url(r'^demo',views.userhomepage,name='Demo_homepage'),
    url(r'^test',views.test, name='test')

]

