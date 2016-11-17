from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from . import aux

urlpatterns = [

url(r'^$/',views.indexcentralcontrol, name='IndexCentralControl'),
url(r'^testinterface',views.testinterface, name='testinterface'),
url(r'^functiontest',aux.functiontest, name='functiontest'),






]

