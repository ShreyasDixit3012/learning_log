# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:01:18 2020

@author: Shreyas Dixit
"""


from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets= {'text': forms.Textarea(attrs={'cols': 80})} 