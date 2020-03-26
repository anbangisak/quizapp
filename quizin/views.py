from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from quizin.models import Question, Answer
from quizin.forms import QuizForm, UserLogin, AdminLogin


def index(request):

    #TODO: change it to login
    default_user = User.objects.get(pk=1)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data.get("Question")
            quz = Question(quest=question, user=default_user)
            quz.save()
            quz.save_answers(form)
            return HttpResponseRedirect('/')
    else:
        template = loader.get_template('quizin/index.html')
        form = QuizForm()
        context = {
            'page_name': 'Add Quiz With MultiChoice Answers',
            'form': form
        }
        return HttpResponse(template.render(context, request))

    # return render(request, 'quizin/index.html', {'form': form})

def list_questions(request):
    quests = Questions.objects.all()
    usr = User.objects.get(email=request.session.get('email'))
    return render(request, 'quizin/list_questions.html', {'page_name': 'User Quiz Page', 'questions': quests})

def quiz_user_login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            usr = User.objects.get_or_create(email=email)
            request.session['email'] = email
            usr.save()
            return HttpResponseRedirect('/list_questions')
    return render(request, 'quizin/email_login.html', {'page_name': 'User Login Quiz Page'})

def quiz_admin_user_login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            request.session['username'] = username
            usr.save()
            return HttpResponseRedirect('/csv_out')
    return render(request, 'quizin/admin_user_login.html', {'page_name': 'Admin Login Quiz Page'})