from django import forms
from .models import Post, Lesson


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('lesson_type', 'lesson_description')
