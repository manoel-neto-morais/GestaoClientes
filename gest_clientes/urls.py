from django.contrib import admin
from django.urls import path, include
from .clientes import urls as urls_clientes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(urls_clientes))
]
