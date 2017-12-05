from django.conf.urls import url
from apps.documentos.views import Index, Nosotros, Puntos, NuestraEmpresa
urlpatterns = [
    url(r'^index', Index.as_view(),name='index'),
    url(r'^nosotros', Nosotros.as_view(),name='nosotros'),
    url(r'^puntos', Puntos.as_view(),name='puntos'),
    url(r'^nuestra_empresa', NuestraEmpresa.as_view(),name='empresa'),
]