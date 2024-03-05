import datetime

from django.utils import timezone
from django.db import models
class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField('Author', on_delete=models.CASCADE, primary_key=True)

class Author(models.Model):
    name = models.CharField(max_length=10)
    desciption = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Category(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=50)
    img = models.ImageField(upload_to='images')
    objects = models.Manager()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
#news add likes
class Article(models.Model):
    title = models.CharField('Название',max_length=50)
    anons = models.CharField('Анонс', max_length=250,blank=True)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации', default=datetime.date.today, null=True, blank=True)

    def ___str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
