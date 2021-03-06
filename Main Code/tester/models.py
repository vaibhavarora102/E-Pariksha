from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class MCQ10TestQuestion(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=250, unique=True)
    test_key = models.CharField(max_length=250, unique=True, primary_key=True)
    
    date_created = models.DateTimeField(default=timezone.now)


    question_1 = models.CharField(max_length=250, blank=True )
    option_1_a = models.CharField(max_length = 150, blank=True )
    option_1_b = models.CharField(max_length = 150, blank=True )
    option_1_c = models.CharField(max_length = 150, blank=True )
    option_1_d = models.CharField(max_length = 150, blank=True )
    
    question_2 = models.CharField(max_length=250, blank=True )
    option_2_a = models.CharField(max_length = 150, blank=True )
    option_2_b = models.CharField(max_length = 150, blank=True )
    option_2_c = models.CharField(max_length = 150, blank=True )
    option_2_d = models.CharField(max_length = 150, blank=True )
    
    question_3 = models.CharField(max_length=250, blank=True )
    option_3_a = models.CharField(max_length = 150, blank=True )
    option_3_b = models.CharField(max_length = 150, blank=True )
    option_3_c = models.CharField(max_length = 150, blank=True )
    option_3_d = models.CharField(max_length = 150, blank=True )
    
    question_4 = models.CharField(max_length=250, blank=True )
    option_4_a = models.CharField(max_length = 150, blank=True )
    option_4_b = models.CharField(max_length = 150, blank=True )
    option_4_c = models.CharField(max_length = 150, blank=True )
    option_4_d = models.CharField(max_length = 150, blank=True )
    
    question_5 = models.CharField(max_length=250, blank=True )
    option_5_a = models.CharField(max_length = 150, blank=True )
    option_5_b = models.CharField(max_length = 150, blank=True )
    option_5_c = models.CharField(max_length = 150, blank=True )
    option_5_d = models.CharField(max_length = 150, blank=True )
    
    question_6 = models.CharField(max_length=250, blank=True )
    option_6_a = models.CharField(max_length = 150, blank=True )
    option_6_b = models.CharField(max_length = 150, blank=True )
    option_6_c = models.CharField(max_length = 150, blank=True )
    option_6_d = models.CharField(max_length = 150, blank=True )
    
    question_7 = models.CharField(max_length=250, blank=True )
    option_7_a = models.CharField(max_length = 150, blank=True )
    option_7_b = models.CharField(max_length = 150, blank=True )
    option_7_c = models.CharField(max_length = 150, blank=True )
    option_7_d = models.CharField(max_length = 150, blank=True )
    
    question_8 = models.CharField(max_length=250, blank=True )
    option_8_a = models.CharField(max_length = 150, blank=True )
    option_8_b = models.CharField(max_length = 150, blank=True )
    option_8_c = models.CharField(max_length = 150, blank=True )
    option_8_d = models.CharField(max_length = 150, blank=True )
    
    question_9 = models.CharField(max_length=250, blank=True )
    option_9_a = models.CharField(max_length = 150, blank=True )
    option_9_b = models.CharField(max_length = 150, blank=True )
    option_9_c = models.CharField(max_length = 150, blank=True )
    option_9_d = models.CharField(max_length = 150, blank=True )
    
    question_10 = models.CharField(max_length=250, blank=True )
    option_10_a = models.CharField(max_length = 150, blank=True )
    option_10_b = models.CharField(max_length = 150, blank=True )
    option_10_c = models.CharField(max_length = 150, blank=True )
    option_10_d = models.CharField(max_length = 150, blank=True )
    

    def get_absolute_url(self):
        return reverse('home-paper')

class MCQ25TestQuestion(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=250, unique=True)
    test_key = models.CharField(max_length=250, unique=True, primary_key=True)
    date_created = models.DateTimeField(default=timezone.now)

    
    question_1 = models.CharField(max_length=250, blank=True )
    option_1_a = models.CharField(max_length = 150, blank=True )
    option_1_b = models.CharField(max_length = 150, blank=True )
    option_1_c = models.CharField(max_length = 150, blank=True )
    option_1_d = models.CharField(max_length = 150, blank=True )
    
    question_2 = models.CharField(max_length=250, blank=True )
    option_2_a = models.CharField(max_length = 150, blank=True )
    option_2_b = models.CharField(max_length = 150, blank=True )
    option_2_c = models.CharField(max_length = 150, blank=True )
    option_2_d = models.CharField(max_length = 150, blank=True )
    
    question_3 = models.CharField(max_length=250, blank=True )
    option_3_a = models.CharField(max_length = 150, blank=True )
    option_3_b = models.CharField(max_length = 150, blank=True )
    option_3_c = models.CharField(max_length = 150, blank=True )
    option_3_d = models.CharField(max_length = 150, blank=True )
    
    question_4 = models.CharField(max_length=250, blank=True )
    option_4_a = models.CharField(max_length = 150, blank=True )
    option_4_b = models.CharField(max_length = 150, blank=True )
    option_4_c = models.CharField(max_length = 150, blank=True )
    option_4_d = models.CharField(max_length = 150, blank=True )
    
    question_5 = models.CharField(max_length=250, blank=True )
    option_5_a = models.CharField(max_length = 150, blank=True )
    option_5_b = models.CharField(max_length = 150, blank=True )
    option_5_c = models.CharField(max_length = 150, blank=True )
    option_5_d = models.CharField(max_length = 150, blank=True )
    
    question_6 = models.CharField(max_length=250, blank=True )
    option_6_a = models.CharField(max_length = 150, blank=True )
    option_6_b = models.CharField(max_length = 150, blank=True )
    option_6_c = models.CharField(max_length = 150, blank=True )
    option_6_d = models.CharField(max_length = 150, blank=True )
    
    question_7 = models.CharField(max_length=250, blank=True )
    option_7_a = models.CharField(max_length = 150, blank=True )
    option_7_b = models.CharField(max_length = 150, blank=True )
    option_7_c = models.CharField(max_length = 150, blank=True )
    option_7_d = models.CharField(max_length = 150, blank=True )
    
    question_8 = models.CharField(max_length=250, blank=True )
    option_8_a = models.CharField(max_length = 150, blank=True )
    option_8_b = models.CharField(max_length = 150, blank=True )
    option_8_c = models.CharField(max_length = 150, blank=True )
    option_8_d = models.CharField(max_length = 150, blank=True )
    
    question_9 = models.CharField(max_length=250, blank=True )
    option_9_a = models.CharField(max_length = 150, blank=True )
    option_9_b = models.CharField(max_length = 150, blank=True )
    option_9_c = models.CharField(max_length = 150, blank=True )
    option_9_d = models.CharField(max_length = 150, blank=True )
    
    question_10 = models.CharField(max_length=250, blank=True )
    option_10_a = models.CharField(max_length = 150, blank=True )
    option_10_b = models.CharField(max_length = 150, blank=True )
    option_10_c = models.CharField(max_length = 150, blank=True )
    option_10_d = models.CharField(max_length = 150, blank=True )
    question_11 = models.CharField(max_length=250, blank=True )
    option_11_a = models.CharField(max_length = 150, blank=True )
    option_11_b = models.CharField(max_length = 150, blank=True )
    option_11_c = models.CharField(max_length = 150, blank=True )
    option_11_d = models.CharField(max_length = 150, blank=True )
    
    question_12 = models.CharField(max_length=250, blank=True )
    option_12_a = models.CharField(max_length = 150, blank=True )
    option_12_b = models.CharField(max_length = 150, blank=True )
    option_12_c = models.CharField(max_length = 150, blank=True )
    option_12_d = models.CharField(max_length = 150, blank=True )
    
    question_13 = models.CharField(max_length=250, blank=True )
    option_13_a = models.CharField(max_length = 150, blank=True )
    option_13_b = models.CharField(max_length = 150, blank=True )
    option_13_c = models.CharField(max_length = 150, blank=True )
    option_13_d = models.CharField(max_length = 150, blank=True )
    
    question_14 = models.CharField(max_length=250, blank=True )
    option_14_a = models.CharField(max_length = 150, blank=True )
    option_14_b = models.CharField(max_length = 150, blank=True )
    option_14_c = models.CharField(max_length = 150, blank=True )
    option_14_d = models.CharField(max_length = 150, blank=True )
    
    question_15 = models.CharField(max_length=250, blank=True )
    option_15_a = models.CharField(max_length = 150, blank=True )
    option_15_b = models.CharField(max_length = 150, blank=True )
    option_15_c = models.CharField(max_length = 150, blank=True )
    option_15_d = models.CharField(max_length = 150, blank=True )
    
    question_16 = models.CharField(max_length=250, blank=True )
    option_16_a = models.CharField(max_length = 150, blank=True )
    option_16_b = models.CharField(max_length = 150, blank=True )
    option_16_c = models.CharField(max_length = 150, blank=True )
    option_16_d = models.CharField(max_length = 150, blank=True )
    
    question_17 = models.CharField(max_length=250, blank=True )
    option_17_a = models.CharField(max_length = 150, blank=True )
    option_17_b = models.CharField(max_length = 150, blank=True )
    option_17_c = models.CharField(max_length = 150, blank=True )
    option_17_d = models.CharField(max_length = 150, blank=True )
    
    question_18 = models.CharField(max_length=250, blank=True )
    option_18_a = models.CharField(max_length = 150, blank=True )
    option_18_b = models.CharField(max_length = 150, blank=True )
    option_18_c = models.CharField(max_length = 150, blank=True )
    option_18_d = models.CharField(max_length = 150, blank=True )
    
    question_19 = models.CharField(max_length=250, blank=True )
    option_19_a = models.CharField(max_length = 150, blank=True )
    option_19_b = models.CharField(max_length = 150, blank=True )
    option_19_c = models.CharField(max_length = 150, blank=True )
    option_19_d = models.CharField(max_length = 150, blank=True )
    
    question_20 = models.CharField(max_length=250, blank=True )
    option_20_a = models.CharField(max_length = 150, blank=True )
    option_20_b = models.CharField(max_length = 150, blank=True )
    option_20_c = models.CharField(max_length = 150, blank=True )
    option_20_d = models.CharField(max_length = 150, blank=True )

    question_21 = models.CharField(max_length=250, blank=True )
    option_21_a = models.CharField(max_length = 150, blank=True )
    option_21_b = models.CharField(max_length = 150, blank=True )
    option_21_c = models.CharField(max_length = 150, blank=True )
    option_21_d = models.CharField(max_length = 150, blank=True )
    
    question_22 = models.CharField(max_length=250, blank=True )
    option_22_a = models.CharField(max_length = 150, blank=True )
    option_22_b = models.CharField(max_length = 150, blank=True )
    option_22_c = models.CharField(max_length = 150, blank=True )
    option_22_d = models.CharField(max_length = 150, blank=True )
    
    question_23 = models.CharField(max_length=250, blank=True )
    option_23_a = models.CharField(max_length = 150, blank=True )
    option_23_b = models.CharField(max_length = 150, blank=True )
    option_23_c = models.CharField(max_length = 150, blank=True )
    option_23_d = models.CharField(max_length = 150, blank=True )
    
    question_24 = models.CharField(max_length=250, blank=True )
    option_24_a = models.CharField(max_length = 150, blank=True )
    option_24_b = models.CharField(max_length = 150, blank=True )
    option_24_c = models.CharField(max_length = 150, blank=True )
    option_24_d = models.CharField(max_length = 150, blank=True )
    
    question_25 = models.CharField(max_length=250, blank=True )
    option_25_a = models.CharField(max_length = 150, blank=True )
    option_25_b = models.CharField(max_length = 150, blank=True )
    option_25_c = models.CharField(max_length = 150, blank=True )
    option_25_d = models.CharField(max_length = 150, blank=True )


    def get_absolute_url(self):
        return reverse('home-paper')

class QuestionAndAnsweer10TestQuestion(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=250, unique=True)
    test_key = models.CharField(max_length=250, unique=True, primary_key=True)
    date_created = models.DateTimeField(default=timezone.now)


    question_1 = models.CharField(max_length=250, blank=True )
    question_2 = models.CharField(max_length=250, blank=True )
    question_3 = models.CharField(max_length=250, blank=True )
    question_4 = models.CharField(max_length=250, blank=True )
    question_5 = models.CharField(max_length=250, blank=True )
    question_6 = models.CharField(max_length=250, blank=True )
    question_7 = models.CharField(max_length=250, blank=True )
    question_8 = models.CharField(max_length=250, blank=True )
    question_9 = models.CharField(max_length=250, blank=True )
    question_10 = models.CharField(max_length=250, blank=True )



    def get_absolute_url(self):
        return reverse('home-paper')

class ansQnA10(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.ForeignKey(QuestionAndAnsweer10TestQuestion,on_delete=models.CASCADE, primary_key=True)


    answer_1 = models.CharField(max_length=1000, blank=True )
    answer_2 = models.CharField(max_length=1000, blank=True )
    answer_3 = models.CharField(max_length=1000, blank=True )
    answer_4 = models.CharField(max_length=1000, blank=True )
    answer_5 = models.CharField(max_length=1000, blank=True )
    answer_6 = models.CharField(max_length=1000, blank=True )
    answer_7 = models.CharField(max_length=1000, blank=True )
    answer_8 = models.CharField(max_length=1000, blank=True )
    answer_9 = models.CharField(max_length=1000, blank=True )
    answer_10 = models.CharField(max_length=1000, blank=True )
    def __str__(self):
        return self.student.username
    def get_absolute_url(self):
        return reverse('home-paper')
   
class ansMCQ10(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.ForeignKey(MCQ10TestQuestion,on_delete=models.CASCADE, primary_key=True)


    answer_1 = models.CharField(max_length=1000, blank=True )
    answer_2 = models.CharField(max_length=1000, blank=True )
    answer_3 = models.CharField(max_length=1000, blank=True )
    answer_4 = models.CharField(max_length=1000, blank=True )
    answer_5 = models.CharField(max_length=1000, blank=True )
    answer_6 = models.CharField(max_length=1000, blank=True )
    answer_7 = models.CharField(max_length=1000, blank=True )
    answer_8 = models.CharField(max_length=1000, blank=True )
    answer_9 = models.CharField(max_length=1000, blank=True )
    answer_10 = models.CharField(max_length=1000, blank=True )
    def __str__(self):
        return self.test_name
    def get_absolute_url(self):
        return reverse('home-paper')

class ansMCQ25(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.ForeignKey(MCQ25TestQuestion,on_delete=models.CASCADE, primary_key=True)


    answer_1 = models.CharField(max_length=1000, blank=True )
    answer_2 = models.CharField(max_length=1000, blank=True )
    answer_3 = models.CharField(max_length=1000, blank=True )
    answer_4 = models.CharField(max_length=1000, blank=True )
    answer_5 = models.CharField(max_length=1000, blank=True )
    answer_6 = models.CharField(max_length=1000, blank=True )
    answer_7 = models.CharField(max_length=1000, blank=True )
    answer_8 = models.CharField(max_length=1000, blank=True )
    answer_9 = models.CharField(max_length=1000, blank=True )
    answer_10 = models.CharField(max_length=1000, blank=True )
    answer_11 = models.CharField(max_length=1000, blank=True )
    answer_12 = models.CharField(max_length=1000, blank=True )
    answer_13 = models.CharField(max_length=1000, blank=True )
    answer_14 = models.CharField(max_length=1000, blank=True )
    answer_15 = models.CharField(max_length=1000, blank=True )
    answer_16 = models.CharField(max_length=1000, blank=True )
    answer_17 = models.CharField(max_length=1000, blank=True )
    answer_18 = models.CharField(max_length=1000, blank=True )
    answer_19 = models.CharField(max_length=1000, blank=True )
    answer_20 = models.CharField(max_length=1000, blank=True )
    answer_21 = models.CharField(max_length=1000, blank=True )
    answer_22 = models.CharField(max_length=1000, blank=True )
    answer_23 = models.CharField(max_length=1000, blank=True )
    answer_24 = models.CharField(max_length=1000, blank=True )
    answer_25 = models.CharField(max_length=1000, blank=True )

    def __str__(self):
        return self.test_name
    def get_absolute_url(self):
        return reverse('home-paper')