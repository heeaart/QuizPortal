from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=1024)
    surname = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    isActive = models.BooleanField(default=True)
    registrationDate = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    tekst = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shuffleAnswers = models.BooleanField(default=True)

class Answer(models.Model):
    tekst = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answerOrder = models.IntegerField(default=1)
    isCorrect = models.BooleanField(default=False)

class Quiz(models.Model):
    class Meta:
        verbose_name_plural = "Kłuizes"
    questions = models.ManyToManyField(Question)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

