# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import  HttpResponse
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string

from stackhub.models import (
    Question,
    Tag,
    Answer,
)
from stackhub.forms import (
    PostQuestionForm,
    QuestionDetailForm,
    ProfileForm,




)

def home(request):
    return render(request, 'stackhub/home.html')


def search(request):
    query = request.GET.get('q')

    questions = Question.objects.filter(title__icontains=query)
    response = render_to_string('stackhub/search_results.html', {'questions': questions})
    # import ipdb; ipdb.set_trace()

    response = json.dumps({'result_page': response})

    return HttpResponse(response, content_type='application/json')

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request,'post_questionpage.html')

def logout_page(request):
    logout(request)
    return redirect(reverse('login'))

# def home_page(request):


# @login_required((login_url='/stackhub/login/'))
def post_questionpage(request):
    if request.method == 'POST':
        form =  PostQuestionForm(data=request.POST)
        if form.is_valid():
            q = form.save()
            return redirect(reverse('question_detailpage', kwargs={'q_id': q.id}))
    else:
        form =  PostQuestionForm(initial={'user': request.user})
    return render(request, 'stackhub/post_questionpage.html', {'question_form': form})

def question_detailpage(request, q_id):

    # print (vars(request), 'request')
    if request.method == 'POST':
        answer = request.POST['answer']

        # answer object
        # Answer = object.create
        try:
            answer = Answer.objects.create(
                answer=answer, user=request.user, question_id=q_id
            )
            response = {'success': True}
        except:
            response = {'success': False}
        return HttpResponse(json.dumps(response), content_type='application/json')


    question = Question.objects.get(id=q_id)
    answers = Answer.objects.filter(question=question)
    # answer = Answer.objects.get(current_question)

    # if rqeust.method == 'POST':

    return render(
        request,
        'stackhub/question_detailpage.html',
        {
            'question': question,
            'answers': answers
        }
    )

def profile_page(request):




    # if request.method == 'POST':
    #     form = ProfileForm(data=request.POST, instance=request.user)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form =  ProfileForm(instance=request.user)
    asked_questions = 
    answered_questions =
    return render(request, 'stackhub/profile_page.html')

# def answer_update(request, q_id):
#     question_id = Question.objects.get(id=q_id)
#
#     return render(request,'stackhub/question_detailpage.html',{'answer':answer,'question_id':question_id})

#
# def search_resultpage(request):


# def user_profilepage(request):
