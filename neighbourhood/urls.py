from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
     url(r'^House/(?P<id>[0-9]+)$',views.house, name='House'),
    url(r'^room/(?P<id>[0-9]+)$',views.room, name='Room'),
url(r'^$',views.indexneighbourhood, name='IndexNeighbourhood'),




]

