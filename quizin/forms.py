from django import forms

class QuizForm(forms.Form):
    Question = forms.CharField(label='Questions is. ', max_length=1000)
    answer1 = forms.CharField(label='Answer1 ', max_length=500)
    answer2 = forms.CharField(label='Answer2', max_length=500)
    answer3 = forms.CharField(label='Answer3', max_length=500)
    answer4 = forms.CharField(label='Answer4', max_length=500)
    correct_answer = forms.IntegerField(label='Give the number that is correct answer ')
