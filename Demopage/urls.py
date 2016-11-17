from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Demo_homepage, name='index'),
    url(r'^Uitleg',views.demo_uitleg,name='Demo_uitleg'),
    url(r'^contact',views.contact,name='Contact_page')


]

