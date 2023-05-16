from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=1024)
    name = models.EmailField(max_length=200)
    surname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)
    registrationDate = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    tekst = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    shuffleAnswers = models.BooleanField(default=True)

class Answer(models.Model):
    tekst = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class QuestionAnswers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answerOrder = models.IntegerField(default=1)
    isCorrect = models.BooleanField()

class quiz(models.Model):
    questions = models.ManyToManyField(Question)
    author = models.ForeignKey(User, on_delete=models.CASCADE)