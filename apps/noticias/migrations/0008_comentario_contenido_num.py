# Generated by Django 3.2 on 2022-09-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0007_alter_comentario_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='contenido_num',
            field=models.TextField(default='x'),
        ),
    ]