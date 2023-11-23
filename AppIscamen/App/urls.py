from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from .views import login_view, recp_pupa_form, produccion_form, produccion_success, salir, liberacion_form, liberacion_success

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_view, name='login'),
    path('recp_pupa_form/', recp_pupa_form, name='recp_pupa_form'),
    path('produccion/', produccion_form, name='produccion_form'),
    path('produccion/success/', produccion_success, name='produccion_success'),
    path('salir/', salir, name='salir'),
    path('liberacion/', liberacion_form, name='liberacion_form'),
    path('liberacion/success/', liberacion_success, name='liberacion_success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)