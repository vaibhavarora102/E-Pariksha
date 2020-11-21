from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class MCQ10TestQuestion(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.TextField(unique=True)
    test_key = models.TextField(unique=True)
    
    date_created = models.DateTimeField(default=timezone.now)
    date_and_time_for_test_to_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_and_time_for_test_to_end = models.DateTimeField(auto_now=False, auto_now_add=False)

    question_1 = models.CharField(max_length=250)
    option_1_a = models.CharField(max_length = 150)
    option_1_b = models.CharField(max_length = 150)
    option_1_c = models.CharField(max_length = 150)
    option_1_d = models.CharField(max_length = 150)
    
    question_2 = models.CharField(max_length=250)
    option_2_a = models.CharField(max_length = 150)
    option_2_b = models.CharField(max_length = 150)
    option_2_c = models.CharField(max_length = 150)
    option_2_d = models.CharField(max_length = 150)
    
    question_3 = models.CharField(max_length=250)
    option_3_a = models.CharField(max_length = 150)
    option_3_b = models.CharField(max_length = 150)
    option_3_c = models.CharField(max_length = 150)
    option_3_d = models.CharField(max_length = 150)
    
    question_4 = models.CharField(max_length=250)
    option_4_a = models.CharField(max_length = 150)
    option_4_b = models.CharField(max_length = 150)
    option_4_c = models.CharField(max_length = 150)
    option_4_d = models.CharField(max_length = 150)
    
    question_5 = models.CharField(max_length=250)
    option_5_a = models.CharField(max_length = 150)
    option_5_b = models.CharField(max_length = 150)
    option_5_c = models.CharField(max_length = 150)
    option_5_d = models.CharField(max_length = 150)
    
    question_6 = models.CharField(max_length=250)
    option_6_a = models.CharField(max_length = 150)
    option_6_b = models.CharField(max_length = 150)
    option_6_c = models.CharField(max_length = 150)
    option_6_d = models.CharField(max_length = 150)
    
    question_7 = models.CharField(max_length=250)
    option_7_a = models.CharField(max_length = 150)
    option_7_b = models.CharField(max_length = 150)
    option_7_c = models.CharField(max_length = 150)
    option_7_d = models.CharField(max_length = 150)
    
    question_8 = models.CharField(max_length=250)
    option_8_a = models.CharField(max_length = 150)
    option_8_b = models.CharField(max_length = 150)
    option_8_c = models.CharField(max_length = 150)
    option_8_d = models.CharField(max_length = 150)
    
    question_9 = models.CharField(max_length=250)
    option_9_a = models.CharField(max_length = 150)
    option_9_b = models.CharField(max_length = 150)
    option_9_c = models.CharField(max_length = 150)
    option_9_d = models.CharField(max_length = 150)
    
    question_10 = models.CharField(max_length=250)
    option_10_a = models.CharField(max_length = 150)
    option_10_b = models.CharField(max_length = 150)
    option_10_c = models.CharField(max_length = 150)
    option_10_d = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.test_name
    def get_absolute_url(self):
        return reverse('created')

class MCQ25TestQuestion(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.TextField(unique=True)
    test_key = models.TextField(unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_and_time_for_test_to_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_and_time_for_test_to_end = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    question_1 = models.CharField(max_length=250)
    option_1_a = models.CharField(max_length = 150)
    option_1_b = models.CharField(max_length = 150)
    option_1_c = models.CharField(max_length = 150)
    option_1_d = models.CharField(max_length = 150)
    
    question_2 = models.CharField(max_length=250)
    option_2_a = models.CharField(max_length = 150)
    option_2_b = models.CharField(max_length = 150)
    option_2_c = models.CharField(max_length = 150)
    option_2_d = models.CharField(max_length = 150)
    
    question_3 = models.CharField(max_length=250)
    option_3_a = models.CharField(max_length = 150)
    option_3_b = models.CharField(max_length = 150)
    option_3_c = models.CharField(max_length = 150)
    option_3_d = models.CharField(max_length = 150)
    
    question_4 = models.CharField(max_length=250)
    option_4_a = models.CharField(max_length = 150)
    option_4_b = models.CharField(max_length = 150)
    option_4_c = models.CharField(max_length = 150)
    option_4_d = models.CharField(max_length = 150)
    
    question_5 = models.CharField(max_length=250)
    option_5_a = models.CharField(max_length = 150)
    option_5_b = models.CharField(max_length = 150)
    option_5_c = models.CharField(max_length = 150)
    option_5_d = models.CharField(max_length = 150)
    
    question_6 = models.CharField(max_length=250)
    option_6_a = models.CharField(max_length = 150)
    option_6_b = models.CharField(max_length = 150)
    option_6_c = models.CharField(max_length = 150)
    option_6_d = models.CharField(max_length = 150)
    
    question_7 = models.CharField(max_length=250)
    option_7_a = models.CharField(max_length = 150)
    option_7_b = models.CharField(max_length = 150)
    option_7_c = models.CharField(max_length = 150)
    option_7_d = models.CharField(max_length = 150)
    
    question_8 = models.CharField(max_length=250)
    option_8_a = models.CharField(max_length = 150)
    option_8_b = models.CharField(max_length = 150)
    option_8_c = models.CharField(max_length = 150)
    option_8_d = models.CharField(max_length = 150)
    
    question_9 = models.CharField(max_length=250)
    option_9_a = models.CharField(max_length = 150)
    option_9_b = models.CharField(max_length = 150)
    option_9_c = models.CharField(max_length = 150)
    option_9_d = models.CharField(max_length = 150)
    
    question_10 = models.CharField(max_length=250)
    option_10_a = models.CharField(max_length = 150)
    option_10_b = models.CharField(max_length = 150)
    option_10_c = models.CharField(max_length = 150)
    option_10_d = models.CharField(max_length = 150)
    question_11 = models.CharField(max_length=250)
    option_11_a = models.CharField(max_length = 150)
    option_11_b = models.CharField(max_length = 150)
    option_11_c = models.CharField(max_length = 150)
    option_11_d = models.CharField(max_length = 150)
    
    question_12 = models.CharField(max_length=250)
    option_12_a = models.CharField(max_length = 150)
    option_12_b = models.CharField(max_length = 150)
    option_12_c = models.CharField(max_length = 150)
    option_12_d = models.CharField(max_length = 150)
    
    question_13 = models.CharField(max_length=250)
    option_13_a = models.CharField(max_length = 150)
    option_13_b = models.CharField(max_length = 150)
    option_13_c = models.CharField(max_length = 150)
    option_13_d = models.CharField(max_length = 150)
    
    question_14 = models.CharField(max_length=250)
    option_14_a = models.CharField(max_length = 150)
    option_14_b = models.CharField(max_length = 150)
    option_14_c = models.CharField(max_length = 150)
    option_14_d = models.CharField(max_length = 150)
    
    question_15 = models.CharField(max_length=250)
    option_15_a = models.CharField(max_length = 150)
    option_15_b = models.CharField(max_length = 150)
    option_15_c = models.CharField(max_length = 150)
    option_15_d = models.CharField(max_length = 150)
    
    question_16 = models.CharField(max_length=250)
    option_16_a = models.CharField(max_length = 150)
    option_16_b = models.CharField(max_length = 150)
    option_16_c = models.CharField(max_length = 150)
    option_16_d = models.CharField(max_length = 150)
    
    question_17 = models.CharField(max_length=250)
    option_17_a = models.CharField(max_length = 150)
    option_17_b = models.CharField(max_length = 150)
    option_17_c = models.CharField(max_length = 150)
    option_17_d = models.CharField(max_length = 150)
    
    question_18 = models.CharField(max_length=250)
    option_18_a = models.CharField(max_length = 150)
    option_18_b = models.CharField(max_length = 150)
    option_18_c = models.CharField(max_length = 150)
    option_18_d = models.CharField(max_length = 150)
    
    question_19 = models.CharField(max_length=250)
    option_19_a = models.CharField(max_length = 150)
    option_19_b = models.CharField(max_length = 150)
    option_19_c = models.CharField(max_length = 150)
    option_19_d = models.CharField(max_length = 150)
    
    question_20 = models.CharField(max_length=250)
    option_20_a = models.CharField(max_length = 150)
    option_20_b = models.CharField(max_length = 150)
    option_20_c = models.CharField(max_length = 150)
    option_20_d = models.CharField(max_length = 150)

    question_21 = models.CharField(max_length=250)
    option_21_a = models.CharField(max_length = 150)
    option_21_b = models.CharField(max_length = 150)
    option_21_c = models.CharField(max_length = 150)
    option_21_d = models.CharField(max_length = 150)
    
    question_22 = models.CharField(max_length=250)
    option_22_a = models.CharField(max_length = 150)
    option_22_b = models.CharField(max_length = 150)
    option_22_c = models.CharField(max_length = 150)
    option_22_d = models.CharField(max_length = 150)
    
    question_23 = models.CharField(max_length=250)
    option_23_a = models.CharField(max_length = 150)
    option_23_b = models.CharField(max_length = 150)
    option_23_c = models.CharField(max_length = 150)
    option_23_d = models.CharField(max_length = 150)
    
    question_24 = models.CharField(max_length=250)
    option_24_a = models.CharField(max_length = 150)
    option_24_b = models.CharField(max_length = 150)
    option_24_c = models.CharField(max_length = 150)
    option_24_d = models.CharField(max_length = 150)
    
    question_25 = models.CharField(max_length=250)
    option_25_a = models.CharField(max_length = 150)
    option_25_b = models.CharField(max_length = 150)
    option_25_c = models.CharField(max_length = 150)
    option_25_d = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.test_name
    def get_absolute_url(self):
        return reverse('created')

class QuestionAndAnsweer10TestQuestion(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.TextField(unique=True)
    test_key = models.TextField(unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_and_time_for_test_to_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_and_time_for_test_to_end = models.DateTimeField(auto_now=False, auto_now_add=False)

    question_1 = models.CharField(max_length=250)
    question_2 = models.CharField(max_length=250)
    question_3 = models.CharField(max_length=250)
    question_4 = models.CharField(max_length=250)
    question_5 = models.CharField(max_length=250)
    question_6 = models.CharField(max_length=250)
    question_7 = models.CharField(max_length=250)
    question_8 = models.CharField(max_length=250)
    question_9 = models.CharField(max_length=250)
    question_10 = models.CharField(max_length=250)


    def __str__(self):
        return self.test_name
    def get_absolute_url(self):
        return reverse('created')