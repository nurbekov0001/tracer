# Generated by Django 3.1.7 on 2021-04-15 08:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0016_auto_20210414_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
