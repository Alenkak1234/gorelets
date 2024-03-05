from django.shortcuts import render, redirect
from django.views import generic
from .models import Article, Category, Author
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.decorators.cache import cache_page
import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

@api_view(['GET', 'POST'])
def manage_items(request, *args, **kwargs):
    if request.method == 'GET':
        items = {}
        count = 0
        print('&&&&&&&&&&&&&&&&&')
        print(redis_instance.keys("*"))
        for key in redis_instance.keys("*"):
            items[key.decode("utf-8")] = redis_instance.get(key)
            count += 1
        response = {
            'count': count,
            'msg': f"Found {count} items.",
            'items': items
        }
        return Response(response, status=200)
    elif request.method == 'POST':
        item = json.loads(request.body)
        key = list(item.keys())[0]
        value = item[key]
        redis_instance.set(key, value)
        response = {
            'msg': f"{key} successfully set to {value}"
        }
        return Response(response, 201)
@api_view(['GET', 'PUT', 'DELETE'])
def manage_item(request, *args, **kwargs):
    if request.method == 'GET':
        if kwargs['key']:
            value = redis_instance.get(kwargs['key'])
            if value:
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': 'success'
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)
    elif request.method == 'PUT':
        if kwargs['key']:
            request_data = json.loads(request.body)
            new_value = request_data['new_value']
            value = redis_instance.get(kwargs['key'])
            if value:
                redis_instance.set(kwargs['key'], new_value)
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': f"Successfully updated {kwargs['key']}"
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

    elif request.method == 'DELETE':
        if kwargs['key']:
            result = redis_instance.delete(kwargs['key'])
            if result == 1:
                response = {
                    'msg': f"{kwargs['key']} successfully deleted"
                }
                return Response(response, status=404)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'news/author_page.html'
    context_object_name = 'author'

def news_home(request):
    news = Article.objects.order_by('-date')
    menu = Category.objects.all()
    print(menu)
    return render(request, 'news/news_home.html', {'news': news, 'menu': menu})

def news_category(request, url):
    news = Article.objects.all()
    menu = Category.objects.filter(url=url)
    return render(request, 'news/news_home.html', {'news': news, 'menu': menu})

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news_delete.html'

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'




def creates(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            error = ''
            return redirect('news_home')
        else:

            error = 'Форма заполнена неверно'
    form = ArticleForm(request.POST, request.FILES)#for images you should pass: https://codefellows.github.io/sea-python-401d7/lectures/django_forms.html
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
