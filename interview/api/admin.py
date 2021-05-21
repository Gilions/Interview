from django.contrib import admin

from .models import Answer, Card, Choice, Poll, Question


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'author', 'title', 'start', 'ending', 'description'
    )
    list_filter = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'poll', 'text'
        )
    list_filter = ('text',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'poll', 'author', 'start'
    )
    list_filter = ('author',)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'choise', 'question', 'answer'
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'answer', 'correct')
