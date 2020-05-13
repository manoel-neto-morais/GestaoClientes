# Generated by Django 2.2.4 on 2020-05-04 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]