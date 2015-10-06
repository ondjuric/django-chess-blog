from django.db import models
from django.utils import timezone

__author__ = 'SweetBee'


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image_name = models.CharField(max_length=25, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    lesson_type = models.CharField(max_length=800)
    lesson_description = models.TextField()

    def __str__(self):
        return self.lesson_type
