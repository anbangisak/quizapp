from django import forms

class QuizForm(forms.Form):
    Question = forms.CharField(label='Questions is. ', max_length=1000)
    answer1 = forms.CharField(label='Answer1 ', max_length=500)
    answer2 = forms.CharField(label='Answer2', max_length=500)
    answer3 = forms.CharField(label='Answer3', max_length=500)
    answer4 = forms.CharField(label='Answer4', max_length=500)
    correct_answer = forms.IntegerField(label='Give the number that is correct answer ')


class UserLogin(forms.Form):
	email = forms.EmailField(label='Email Id', max_length=100)


class AdminLogin(forms.Form):
	username = forms.CharField(label='username ', max_length=100)
	password = forms.CharField(label='password ', max_length=100, widget=forms.PasswordInput)