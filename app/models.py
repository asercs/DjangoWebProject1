"""
Definition of models.
"""
from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('News', on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username + " " + self.content

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class News(models.Model):
    title = models.CharField('Название', max_length = 256)
    news_text = models.TextField('Новость')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    

# Create your models here.
