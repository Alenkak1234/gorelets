from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateInput, FileInput, RadioSelect


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'image', 'date', 'author', 'category', 'like']
        widgets = {
            'title': TextInput(attrs={'placeholder': "Название статьи", 'style': 'height:30px;width:700px; font-size:20px;'}),
            'anons': TextInput(attrs={'placeholder': "Анонс статьи", 'style': 'height:30px;width:700px; font-size:20px;'}),
            'full_text': Textarea(attrs={'placeholder': "Текст статьи", 'style': 'height:100px;width:700px; font-size:20px;'}),
            'image': FileInput(attrs={'style': 'height:30px; width:700px; font-size:20px;'}),
            'date': DateInput(attrs={'style': 'height:30px;font-size:20px;'}),
            'like': RadioSelect(attrs={'style': 'height:30px;font-size:20px;'})
        }
