from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    bio = models.TextField(default='')
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    #esta classe é utilizada para definir o nome que será exibido no django-admin para esta classe
    #o parâmetro opcional upload_to defini o diretório que irá manter os arquivos enviados pelos usuários

    def __str__(self):
        return self.first_name
