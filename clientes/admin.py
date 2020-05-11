from django.contrib import admin
from .models import Person #importação do arquivo models

admin.site.register(Person)
