from django.contrib import admin
from .models import MCQ10TestQuestion, MCQ25TestQuestion, QuestionAndAnsweer10TestQuestion, ansQnA10, ansMCQ10, ansMCQ25
# Register your models here.
admin.site.register(MCQ10TestQuestion)
admin.site.register(MCQ25TestQuestion)
admin.site.register(QuestionAndAnsweer10TestQuestion)
admin.site.register(ansQnA10)
admin.site.register(ansMCQ10)
admin.site.register(ansMCQ25)
