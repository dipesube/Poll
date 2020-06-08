# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#every model has a question class
#Question inherits Model

class Question(modles.Model): 
    question_text = modles.CharField(max_length = 200)
    pub_date = models.DateTimeFiel('Date Published')
    def __str__(self):
        return question_text

#Options for user to selection for question
#Choice and question are related using ForeignKey
class Choice(models.Model):
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE )
    choice_text = models.CharFiel(max_length = 200)
    votes = models.IntegerField(default=0)

    #retreive choice text
    def __str__(self):
        return choice_text
