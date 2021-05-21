from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault, HiddenField

from .models import Answer, Card, Choice, Poll, Question


class PollSerializer(serializers.ModelSerializer):
    # Опросы
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Poll
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    # Ответы пользователей
    class Meta:
        model = Answer
        fields = ('number', 'answer', 'correct')


class QuestionSerializerRead(serializers.ModelSerializer):
    # Вывод данных из таблицы Question - только чтение
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'types', 'answers')


class QuestionsSerializerWrite(serializers.ModelSerializer):
    # Запись данных в таблицу Question
    class Meta:
        model = Question
        fields = ('text', 'types')


class UserAnswersSerializer(serializers.ModelSerializer):
    # Вложенный сериалайзер для UserQuestionsSerializer
    class Meta:
        model = Answer
        fields = ('number', 'answer',)


class UserQuestionsSerializer(serializers.ModelSerializer):
    # Вопросы для участников
    answers = UserAnswersSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'types', 'answers',)


class UserChoiceSerializer(serializers.ModelSerializer):
    # Начать участие в опросе
    class Meta:
        model = Choice
        fields = ('start',)

    def validate(self, data):
        request = self.context['request']
        if request.method == "POST":
            poll = request.parser_context['kwargs']['poll_id']
            if Choice.objects.filter(poll=poll, author=request.user).exists():
                raise serializers.ValidationError(
                    'Вы уже участвуете в данном опросе')
        return data


class UserCardSerializer(serializers.ModelSerializer):
    # Запись ответов участников
    class Meta:
        model = Card
        fields = ('answer',)


class UserCardSerializerRead(serializers.ModelSerializer):
    # Вложенный сериалайзер для MeSerializer
    question = serializers.SlugField('question_text')

    class Meta:
        model = Card
        fields = ('question', 'correct_answer', 'answer',)


class MeSerializer(serializers.ModelSerializer):
    # Карточка отвечающего
    poll = serializers.SlugField('poll_title')
    author = serializers.SlugField('author_username')
    cards = UserCardSerializerRead(many=True)

    class Meta:
        model = Choice
        fields = ('poll', 'author', 'start', 'cards')
