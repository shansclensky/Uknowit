# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import  HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login


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

@login_required((login_url='/stackhub/login/'))
def post_questionpage(request):
