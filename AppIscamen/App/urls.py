from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from .views import login_view

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_view, name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)