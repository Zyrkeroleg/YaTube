from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image',)
        labels = {
            'text': 'Текст поста',
            'group': 'Название группы',
            'image': 'Картинка к посту',
        }
        help_texts = {
            'Text': 'Здесь можно написать текст вашего поста',
            'group': 'Группа к которой относится ваш пост',
            'image': 'Можно добавить изображение к посту',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
    labels = {
        'text': 'Текст Коментария',
    }
    help_text = {
        'text': 'Здесь можно написать комментарий',
    }
