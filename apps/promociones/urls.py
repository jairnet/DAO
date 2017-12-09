from django.conf.urls import url
from apps.promociones.views import Promociones
urlpatterns = [
    url(r'^promociones', Promociones.as_view(),name='promociones'),
 ]