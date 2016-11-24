from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from . import aux


urlpatterns = [

url(r'^$',views.indexcentralcontrol, name='IndexCentralControl'),
url(r'^testinterface',views.testinterface, name='testinterface'),
url(r'^ledaan',aux.ledaan, name='ledaan'),
url(r'^leduit',aux.leduit, name='leduit'),
url(r'^led2aan',aux.led2aan, name='led2aan'),
url(r'^led2uit',aux.led2uit, name='led2uit'),
url(r'^led2fel',aux.led2fel, name='led2fel'),
url(r'^led2zwak',aux.led2zwak, name='led2zwak'),


url(r'^doityourself',views.handmatig, name='handmatig'),






]

