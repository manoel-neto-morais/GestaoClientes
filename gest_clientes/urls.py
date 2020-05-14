from django.contrib import admin
from django.urls import path, include
from clientes import urls as urls_clientes
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from home import urls as urls_home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(urls_clientes)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', include(urls_home)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
