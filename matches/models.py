from django.db import models

MAP_CHOICE = (
    ('de_mirage', 'Mirage'),
    ('de_dust2', 'Dust2'),
    ('de_vertigo', 'Vertigo'),
    ('de_nuke', 'Nuke'),
    ('de_inferno', 'Inferno'),
    ('de_overpass', 'Overpass'),
    ('de_train', 'Train'),
    )

class Matches(models.Model):
    tournamentName = models.CharField('Название турнира', max_length = 30)
    team_1 = models.CharField('Первая команда', max_length=30)
    team_2 = models.CharField('Вторая команда', max_length = 30)
    map = models.CharField('Карта', max_length = 30, choices=MAP_CHOICE)
    date = models.DateTimeField('Время матча')

    def __str__(self):
        return self.tournamentName

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

# Create your models here.
