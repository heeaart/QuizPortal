from django.contrib import admin

from .models import User, Question, Answer, QuestionAnswer, Quiz
# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionAnswer)
admin.site.register(Quiz)