from django import forms
from .models import Post, Lesson

__author__ = 'SweetBee'


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image_name')


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('lesson_type', 'lesson_description')
