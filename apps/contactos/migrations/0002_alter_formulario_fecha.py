# Generated by Django 3.2 on 2022-08-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='fecha',
            field=models.DateField(),
        ),
    ]