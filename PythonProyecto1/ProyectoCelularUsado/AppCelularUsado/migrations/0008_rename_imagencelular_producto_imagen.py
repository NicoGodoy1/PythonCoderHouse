# Generated by Django 4.1.7 on 2023-04-16 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCelularUsado', '0007_item_marca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagenCelular',
            new_name='imagen',
        ),
    ]