from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from . import auxilary


urlpatterns = [

url(r'^$',views.indexcentralcontrol, name='IndexCentralControl'),
url(r'^testinterface',views.testinterface, name='testinterface'),
url(r'^ledaan', auxilary.ledaan, name='ledaan'),
url(r'^leduit', auxilary.leduit, name='leduit'),
url(r'^led2aan', auxilary.led2aan, name='led2aan'),
url(r'^led2uit', auxilary.led2uit, name='led2uit'),
url(r'^led2fel', auxilary.led2fel, name='led2fel'),
url(r'^led2zwak', auxilary.led2zwak, name='led2zwak'),

url(r'^status/(?P<appliance_id>[0-9]+)/(?P<status>[0-9]+)$', auxilary.status, name='status'),

url(r'^doityourself',views.handmatig, name='handmatig'),






]

