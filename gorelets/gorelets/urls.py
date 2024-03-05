from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from articles.views import ArticleAPIList, ArticleAPIUpdate, ArticleAPIAll, ArticleAPIModelSet
import debug_toolbar
from rest_framework import routers

#router =

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('api/v1/articlelist/', ArticleAPIModelSet.as_view({'get': 'list'})),
    path('api/v1/articlelist/<int:pk>/', ArticleAPIModelSet.as_view({'put': 'update'})),
    path('__debug__/', include(debug_toolbar.urls))
]
'''
path('api/v1/articlelist/', ArticleAPIList.as_view()),
path('api/v1/articlelist/<int:pk>/', ArticleAPIUpdate.as_view()),
path('api/v1/articledetail/<int:pk>/', ArticleAPIAll.as_view()),
'''


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
