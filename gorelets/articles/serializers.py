from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')


    '''title = serializers.CharField(max_length=50)
    anons = serializers.CharField(read_only=True)
    full_text = serializers.CharField(read_only=True)
    date = serializers.DateField(read_only=True)
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.anons = validated_data.get('anons', instance.anons)
        instance.full_text = validated_data.get('full_text', instance.full_text)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance'''
'''class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'category', 'author')'''