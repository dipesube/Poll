# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Poll Admin"
admin.site.site_title = "Poll Admin Area"
admin.site.index_title = "Welcome"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}), 
    ('Date Information', {'fields': ['pub_date'], 'classes':
    ['collapse']}), ]

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
