# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    tag = models.CharField(max_length = 128)


class Question(models.Model):
    user =  models.ForeignKey(User,on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 150)
    question = models.TextField(max_length = 150)
    tags = models.ManyToManyField(Tag)


class Answer(models.Model):
    created =  models.DateTimeField(default = '2014-02-14')
    updated = models.DateTimeField(default = '2014-02-14')
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    answer = models.TextField(max_length = 256)
