from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import manage_items, manage_item

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.creates, name='create'),
    path('<slug:url>', views.news_category, name='news_category'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>', views.NewsDeleteView.as_view(), name='news_delete'),
    path('<slug:name>', views.AuthorDetailView.as_view(), name = 'author_page'),
    path('all', manage_items, name="items"),
    path('<slug:key>', manage_item, name="single_item")
]
urlpatterns = format_suffix_patterns(urlpatterns)