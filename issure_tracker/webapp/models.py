from django.db import models


class Status(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Статус")

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Тип")

    def __str__(self):
        return f'{self.name}'


class Tracer(models.Model):
    surname = models.CharField(max_length=100, null=False, blank=False, verbose_name="Краткое описание")
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Полное описание")
    status = models.ForeignKey('webapp.Status', related_name='tracers', on_delete=models.PROTECT,
                               verbose_name='Статус')
    type = models.ManyToManyField('webapp.Type', related_name='tracers',
                                  verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        db_table = 'Tracers'
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return f'{self.id}. {self.surname}:{self.description}{self.status} {self.type}'
