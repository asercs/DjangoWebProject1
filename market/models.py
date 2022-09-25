from django.db import models

class Market(models.Model):
    weaponName = models.CharField('Название оружия', max_length = 30)
    skinName = models.CharField('Название скина', max_length=30)
    condition = models.CharField('Качество', max_length = 15)
    price = models.CharField('Цена', max_length = 7)
    float = models.CharField('Флоат', max_length = 8)
    photo = models.TextField('Фото', null=True, blank=True)
    seller = models.TextField('Продавец', null=True)
    seller_url = models.TextField('Ссылка на продавца', null=True)

    def __str__(self):
        return self.weaponName + " " + self.skinName + " " + self.float + " " + self.price

    class Meta:
        verbose_name = 'Маркет'
        verbose_name_plural = 'Маркет'

# Create your models here.
