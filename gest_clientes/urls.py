from django.contrib import admin
from django.urls import path, include
from clientes import urls as urls_clientes
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(urls_clientes)),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
