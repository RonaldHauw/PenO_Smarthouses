from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [

url(r'^$/',views.indexcentralcontrol, name='IndexCentralControl'),
url(r'^testinterface',views.testinterface, name='testinterface'),





]

