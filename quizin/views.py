from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from quizin.models import Question, Answer
from quizin.forms import QuizForm


def index(request):

    template = loader.get_template('quizin/index.html')
    form = QuizForm()
    context = {
        'page_name': 'Add Quiz With MultiChoice Answers',
        'form': form
    }
    return HttpResponse(template.render(context, request))

    # return render(request, 'quizin/index.html', {'form': form})


