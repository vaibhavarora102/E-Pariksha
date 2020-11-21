from django.contrib import admin
from .models import MCQ10TestQuestion, MCQ25TestQuestion, QuestionAndAnsweer10TestQuestion
# Register your models here.
admin.site.register(MCQ10TestQuestion)
admin.site.register(MCQ25TestQuestion)
admin.site.register(QuestionAndAnsweer10TestQuestion)
