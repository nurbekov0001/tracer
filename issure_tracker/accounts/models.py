from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Ползователь')
    bird_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    link = models.URLField(null=True, blank=True, verbose_name='Сылка на GitHub')
    avatar = models.ImageField(null=True, blank=True, verbose_name='Аватар', upload_to='user_pics')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Полное описание")

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
