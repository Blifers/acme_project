# Generated by Django 3.2.16 on 2024-07-23 15:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birthday', '0004_congratulations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Congratulations',
            new_name='Congratulation',
        ),
    ]