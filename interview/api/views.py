from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Answer, Choice, Poll, Question
from .serializers import (AnswerSerializer, MeSerializer, PollSerializer,
                          QuestionSerializerRead, QuestionsSerializerWrite,
                          UserCardSerializer, UserChoiceSerializer,
                          UserQuestionsSerializer)
from .utility import get_author


class AdminPollViewSet(viewsets.ModelViewSet):
    """
    Администрирование таблицы Poll
    Допустимые методы:
    GET, POST, PUT, PATCH, DELETE
    """
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = (IsAdminUser,)


class AdminQuestionViewSet(viewsets.ModelViewSet):
    """
    Администрирование таблицы Question
    Допустимые методы:
    GET, POST, PUT, PATCH, DELETE
    """
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return QuestionSerializerRead
        return QuestionsSerializerWrite

    def get_queryset(self):
        poll = get_object_or_404(
            Poll,
            pk=self.kwargs.get('poll_id')
        )
        return poll.questions.all()

    def perform_create(self, serializer):
        poll = get_object_or_404(
            Poll,
            pk=self.kwargs.get('poll_id')
        )
        return serializer.save(poll=poll)


class AnswerViewSet(viewsets.ModelViewSet):
    """
    Администрирование таблицы Answer
    Доступуп:
    Администратор
    Доступные методы:
    GET, POST, PUT, PATCH, DELETE
    """
    permission_classes = (IsAdminUser,)
    serializer_class = AnswerSerializer
    lookup_field = 'number'

    def get_queryset(self):
        question = get_object_or_404(
            Question,
            pk=self.kwargs.get('q_id')
        )
        queryset = question.answers.all()
        return queryset

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs.get('q_id')
        )
        return serializer.save(question=question)


class PollViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    '''
    Таблица Poll для участников опроса
    Доступ:
    Без ограничений
    Доступные методы:
    GET - List
    '''
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = (AllowAny,)


class QuestionViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    '''
    Таблица Question для участников опроса
    Доступн:
    Без ограничений
    Доступные методы
    GET-List, POST
    '''
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserQuestionsSerializer
        return UserChoiceSerializer

    def get_queryset(self):
        poll = get_object_or_404(
            Poll,
            pk=self.kwargs.get('poll_id')
        )
        return poll.questions.all()

    def perform_create(self, serializer):
        poll = get_object_or_404(
            Poll,
            pk=self.kwargs.get('poll_id')
        )
        author = get_author(self.request.user)
        return serializer.save(poll=poll, author=author)


class CardViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    '''
    Таблица Card для участников опроса
    Доступ без ограничений
    Доступные методы
    GET-List, POST
    '''
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserQuestionsSerializer
        return UserCardSerializer

    def get_queryset(self):
        poll = get_object_or_404(
            Poll,
            pk=self.kwargs.get('poll_id')
        )
        return poll.questions.all()

    def perform_create(self, serializer):
        choise = get_object_or_404(
            Choice,
            author=self.request.user,
            poll=self.kwargs.get('poll_id')
        )
        question = get_object_or_404(
            Question,
            pk=self.kwargs.get('q_id')
        )
        answer_list = list(Answer.objects.all().filter(
            question=question, correct=True).values('number'))
        answer = [i['number'] for i in answer_list]

        return serializer.save(
            choise=choise,
            question=question,
            correct_answer=answer
            )


class MeViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):

    '''
    Отчетность по пройденым опросам
    Доступ:
    Без ограничений
    Доступные методы:
    GET-List
    '''
    permission_classes = (AllowAny,)
    serializer_class = MeSerializer

    def get_queryset(self):
        queryset = self.request.user.choises.all()
        return queryset
