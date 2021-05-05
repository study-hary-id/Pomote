from django.shortcuts import render

from .forms import ChoiceForm, QuestionForm

def home(request):
    return render(request, 'polls/home.html', dict())


def create(request):
    question_form = QuestionForm()
    choice_form = ChoiceForm()

    return render(request, 'polls/create.html', {
        'question_form': question_form,
        'choice_form': choice_form,
    })


def vote(request, poll_id):
    return render(request, 'polls/vote.html', dict())


def result(request, poll_id):
    return render(request, 'polls/result.html', dict())
