from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from stackhub.models import Question,Tag,Answer

class PostQuestionForm(forms.ModelForm):
    tag_input = forms.CharField(label=("Question_tag"))

    class Meta:
        model = Question
        fields = ('title','question', 'tag_input', 'user')
        widgets = {
            'user': forms.widgets.HiddenInput()
        }

    def save(self):
        q_obj = super(PostQuestionForm, self).save()
        tags = self.cleaned_data['tag_input']
        tags_list = tags.split(',')
        tags = []
        for tag in tags_list:
            obj, created = Tag.objects.get_or_create(tag=tag)
            # q_obj.tags.add(obj)
            tags.append(obj)

        q_obj.tags.add(*tags)

        return q_obj

class QuestionDetailForm(forms.ModelForm):
    question = forms.CharField(label=("question"))
    answer =  forms.CharField(label=("answer"))

    class Meta:
        model =  Question
        fields =  ('question','answer')



class ProfileForm(forms.ModelForm):
    question = forms.CharField(label=("question"))
    answer =  forms.CharField(label=("answer"))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','question','answer')

# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model =  Answer
#         fields = ('answer',)
#
#     def save(self):
#         ans = super(AnswerForm,self).save()
#         return ans
