from django.db import models

class Teams(models.Model):
    teamName = models.CharField('Название команды', max_length=30, null=True)
    founder = models.CharField('Создатель', max_length = 30)
    country = models.CharField('Страна', max_length = 30)
    photo = models.TextField('Фото', null=True, blank=True)
    insta = models.CharField('Instagram', max_length = 30, null=True, blank=True)
    vk = models.CharField('VK', max_length = 30, null=True, blank=True)

    def __str__(self):
        return self.teamName

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

# Create your models here.
