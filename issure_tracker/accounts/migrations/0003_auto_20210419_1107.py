# Generated by Django 3.1.7 on 2021-04-19 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210416_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('View_users', 'Просмотр пользоватей')], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
