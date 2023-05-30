from rest_framework import serializers

from .models import User, Question, Quiz


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user', 'email', 'name', 'surname', 'isActive', 'registrationDate')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('tekst', 'author', 'shuffleAnswers')

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('verbose_name_plural', 'questions', 'author')