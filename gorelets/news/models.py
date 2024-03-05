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
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    image = models.ImageField('Изображение', upload_to='images/')
    date = models.DateField('Дата публикации', default=timezone.now)
    '''AUTHORs = Author.objects.all()
    AUTHORS = []
    for i in AUTHORs:
        AUTHORS.append((i.name, i.name))
    CATs = Category.objects.all()
    CATS = []
    for i in CATs:
        CATS.append((i.name, i.name))
    print(AUTHORS, CATS)'''
    author = models.ForeignKey('Author', on_delete = models.CASCADE, null=True)
    category = models.ManyToManyField(Category)
    TYPES = [
        ('LIKE', 'Нравится'),
        ('DISLIKE', 'Не нравится')
    ]
    like = models.CharField("Лайки", choices=TYPES, default='LIKE', max_length=7)

    def ___str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'