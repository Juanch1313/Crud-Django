# Generated by Django 3.2.8 on 2023-03-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_alter_libro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]
