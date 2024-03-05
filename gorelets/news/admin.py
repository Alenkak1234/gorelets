from django.contrib import admin
from .models import Article, Category, Author, Account

admin.site.register(Article)
admin.site.register(Account)
admin.site.register(Author)
admin.site.register(Category)