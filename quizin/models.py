from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Question(models.Model):
    quest = models.CharField(max_length=1000)
    user = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
