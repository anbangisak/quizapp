from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Question(models.Model):
    quest = models.CharField(max_length=1000)
    user = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)

    def save_answers(self, form):
        ans_list = ['answer1', 'answer2', 'answer3', 'answer4']
        ans_list.sort()
        correct_answer = int(form.cleaned_data.get('correct_answer'))
        for idx, field_name in enumerate(ans_list):
            correct = False
            if idx == correct_answer:
                correct = True

            ans = form.cleaned_data.get(field_name)
            ans = Answer(answer=ans, correct=correct, question=self)
            ans.save()

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
