from django.contrib.auth import get_user_model
from django.db import models
from webapp.validator import ErrorValidator, Validator


class Status(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Статус")

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Тип")

    def __str__(self):
        return f'{self.name}'


class Tracer(models.Model):
    surname = models.CharField(max_length=100, null=False, blank=False, verbose_name="Краткое описание",
                               validators=(ErrorValidator(5),))
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Полное описание",
                                   validators=(Validator(['%', '@', '&']),))
    status = models.ForeignKey('webapp.Status', related_name='tracers', on_delete=models.PROTECT,
                               verbose_name='Статус')
    type = models.ManyToManyField('webapp.Type', related_name='tracers',
                                  verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    project = models.ForeignKey('webapp.Project', related_name='tracers', on_delete=models.CASCADE,
                                verbose_name='Проект')

    class Meta:
        db_table = 'Tracers'
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return f'{self.id}. {self.surname}:{self.description}{self.status} {self.type}  '


class Project(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='название')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='описание')
    start_data = models.DateField(auto_now_add=False, verbose_name='Дата начала')
    end_data = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name='Дата окончания')
    user = models.ManyToManyField('auth.User', related_name="projects",
                                  verbose_name='Пользователь')

    class Meta:
        permissions = [
            ('add_delete_change', 'добавлять,удалять,изменять')
        ]

    def __str__(self):
        return f'{self.id}.{self.name} {self.description} {self.start_data}:{self.end_data},{self.user} '
