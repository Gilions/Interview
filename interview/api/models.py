import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

User = get_user_model()


@python_2_unicode_compatible
class Poll(models.Model):
    # Таблица опросов
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Организатор'
    )
    title = models.CharField(
        db_index=True,
        max_length=255,
        verbose_name='Название опроса',
        help_text='Название может быть максимальной длиной до 255 символов.',
    )
    start = models.DateField(
        auto_now_add=True,
        verbose_name='Начало опроса',
    )
    ending = models.DateField(
        verbose_name='Окончание опроса',
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        help_text='Описание опроса.'
    )

    class Meta:
        verbose_name_plural = 'Опросы'
        ordering = ('-start',)

    def __str__(self) -> str:
        return self.title


@python_2_unicode_compatible
class Question(models.Model):
    # Тибалица вопросов
    TYPE = (
        ('TEXT', 'Запишите верный ответ'),
        ('CHOICE', 'Один правильный ответ'),
        ('MULTICHOICE', 'Несколько правильных ответов'),
        )

    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Опрос'
        )
    text = models.TextField(
        verbose_name='Вопрос',
        db_index=True
    )

    types = models.CharField(
        max_length=30,
        choices=TYPE,
        default='TEXT',
        verbose_name='Тип вопроса'
    )

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name_plural = 'Вопросы'


@python_2_unicode_compatible
class Answer(models.Model):
    # Ответы на вопрос
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос',
        help_text='Ответы к данному вопросу'
    )
    number = models.SmallIntegerField(
        verbose_name='Номер ответа',
    )
    answer = models.TextField(
        verbose_name='Ответ'
    )
    correct = models.BooleanField(
        default=False,
        verbose_name='Правильный ответ'
    )

    class Meta:
        verbose_name_plural = 'Ответы'

    def __str__(self) -> str:
        return self.answer


class Choice(models.Model):
    # Участники опросов
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='poll_choise',
        verbose_name='Опрос'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Участник',
        related_name='choises'
    )
    start = models.DateField(
        default=datetime.date.today(),
        editable=False,
        verbose_name='Старт участия'
    )

    class Meta:
        verbose_name_plural = 'Участники вопросов'


class Card(models.Model):
    # Ответы участников
    choise = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        related_name='cards',
        verbose_name='Опрос'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    correct_answer = models.CharField(
        max_length=10,
        verbose_name='Правильный ответ',
        blank=True,
        null=True
    )
    answer = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Ответ автора'
    )

    class Meta:
        verbose_name_plural = 'Карточка автора'
