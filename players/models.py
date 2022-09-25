from django.db import models

class Players(models.Model):
    firstName = models.CharField('Имя', max_length = 30)
    secondName = models.CharField('Фамилия', max_length = 30)
    nickname = models.CharField('Ник', max_length = 30, null=True)
    age = models.IntegerField('Возраст')
    role = models.CharField('Роль', max_length = 20, null=True)
    currentTeam = models.CharField('Команда', max_length = 30)
    country = models.CharField('Страна', max_length = 30)
    insta = models.TextField('Instagram-link', null=True, blank=True)
    vk = models.TextField('VK-link', null=True, blank=True)
    steam = models.TextField('Steam-profile', null=True, blank=True)
    photo = models.TextField('Фото', null=True, blank=True)

    monitor = models.CharField('Монитор', max_length = 30, null=True, blank=True)
    mouse = models.CharField('Мышка', max_length = 30, null=True, blank=True)
    headset = models.CharField('Наушники', max_length = 30, null=True, blank=True)
    mousepad = models.CharField('Коврик', max_length = 30, null=True, blank=True)
    keyboard = models.CharField('Клавиатура', max_length = 30, null=True, blank=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

# Create your models here.

