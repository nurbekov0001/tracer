# Generated by Django 3.1.7 on 2021-03-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20210317_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracer',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Полное описание'),
        ),
    ]
