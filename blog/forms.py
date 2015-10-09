from django import forms
from .models import Post, Lesson

__author__ = 'SweetBee'


class PostForm(forms.ModelForm):
    """
    Lesson Form
    """
    class Meta:
        model = Post
        fields = ('title', 'text', 'image_name')


class LessonForm(forms.ModelForm):
    """
    Lesson Form
    """
    class Meta:
        model = Lesson
        fields = ('lesson_type', 'lesson_description')


class ContactForm(forms.Form):
    """
    Contact Form
    """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(
                              attrs={'placeholder': '* Write message...'}))
