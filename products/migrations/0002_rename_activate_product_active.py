# Generated by Django 4.0.10 on 2024-09-14 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='activate',
            new_name='active',
        ),
    ]
