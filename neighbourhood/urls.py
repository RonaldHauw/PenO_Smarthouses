from django.conf.urls import url
from django.conf.urls.static import static
from . import views
import auxilary

urlpatterns = [
    url(r'^House/(?P<house_id>[0-9]+)$',views.house, name='House'),
    url(r'^House/(?P<house_id>[0-9]+)/chart_data_energy$',views.getchartdata,name='Chartdata'),
    url(r'^room/(?P<id>[0-9]+)$',views.room, name='Room'),
    url(r'^$',views.indexneighbourhood, name='IndexNeighbourhood'),
    url(r'^CentralControl',views.centralcontrol,name="ToCentralControl"),
    url(r'^Root',views.Root,name='Root'),
    url(r'^Demo',views.Demo_homepage,name='Demo'),
    url(r'^$',views.indexcentralcontrol, name='IndexCentralControl'),
    url(r'^testinterface',views.testinterface, name='testinterface'),

    url(r'^status/(?P<appliance_id>[0-9]+)/(?P<parametertochange>[0-9]+)/(?P<value>[0-9]+)$', auxilary.change_status, name='status'),

    url(r'^doityourself',views.handmatig, name='handmatig'),
    url(r'^optimalisated',views.vergelijking, name = 'vergelijking'),


]





