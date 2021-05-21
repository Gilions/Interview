from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AdminPollViewSet, AdminQuestionViewSet, AnswerViewSet,
                    CardViewSet, MeViewSet, PollViewSet, QuestionViewSet)

rounter_v1 = DefaultRouter()

#  Урлы Администратора
rounter_v1.register('admin/polls', AdminPollViewSet, basename='admin_poll')
rounter_v1.register(
    r'admin/polls/(?P<poll_id>\d+)/questions',
    AdminQuestionViewSet,
    basename='admin_question')
rounter_v1.register(
    r'admin/polls/(?P<poll_id>\d+)/questions/(?P<q_id>\d+)/answers',
    AnswerViewSet,
    basename='admin_answers')


# Урлы участников
rounter_v1.register('polls', PollViewSet, basename="user_poll")
rounter_v1.register(
    r'polls/(?P<poll_id>\d+)/questions',
    QuestionViewSet,
    basename='user_questions')
rounter_v1.register(
    r'polls/(?P<poll_id>\d+)/questions/(?P<q_id>\d+)/answers',
    CardViewSet,
    basename='user_card')
rounter_v1.register('me', MeViewSet, basename='me')

urlpatterns = [
    path('api/v1/', include(rounter_v1.urls)),
]
