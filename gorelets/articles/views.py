from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer
from memory_profiler import profile

class ArticleAPIModelSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class ArticleAPIUpdate(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleAPIAll(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


'''class ArticleAPIView(APIView):

    def get(self, request):
        lst = Article.objects.all()
        return Response({'posts': ArticleSerializer(lst, many=True).data})


    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    def put(self,request,*args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response('Method PUT not allowed')
        try:
            instance=Article.objects.get(pk=pk)
        except:
            return Response('Object does not exist')
        serializer = ArticleSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self,request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response('Method DELETE not allowed')
        try:
            instance=Article.objects.get(pk=pk).delete()
        except:
            return Response('Object does not exist')
        return Response({'post': 'Deleted post number ' + str(pk)})'''
'''def get(self, request):
    lst = Article.objects.all().values()
    print(lst)
    return Response({'posts': list(lst)})'''


'''class ArticleAPIView(generics.ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer'''