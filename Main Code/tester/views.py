from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
) 
from .models import MCQ10TestQuestion, MCQ25TestQuestion, QuestionAndAnsweer10TestQuestion

def Created(request):
    return render(request, 'tester/created.html')


def home(request):
    return render(request, 'tester/index.html')

def about(request):
    return render(request, 'tester/about.html')

def contact(request):
    return render(request, 'tester/contact.html')

def pricing(request):
    return render(request, 'tester/pricing.html')

def quiz(request):
    return render(request, 'tester/quiz.html')

def register(request):
    return render(request, 'tester/register.html')

def registerstudent(request):
    return render(request, 'tester/registerstudent.html')








                       ################################
                       #    Create your views here.   #
                       ################################

class MCQ10TestCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MCQ10TestQuestion
    template_name = 'tester/create.html'
    fields = ['test_name','test_key',
                 'question_1', 'option_1_a', 'option_1_b', 'option_1_c', 'option_1_d'
                 'question_2', 'option_2_a', 'option_2_b', 'option_2_c', 'option_2_d'
                 'question_3', 'option_3_a', 'option_3_b', 'option_3_c', 'option_3_d'
                 'question_4', 'option_4_a', 'option_4_b', 'option_4_c', 'option_4_d'
                 'question_5', 'option_5_a', 'option_5_b', 'option_5_c', 'option_5_d'
                 'question_6', 'option_6_a', 'option_6_b', 'option_6_c', 'option_6_d'
                 'question_7', 'option_7_a', 'option_7_b', 'option_7_c', 'option_7_d'
                 'question_8', 'option_8_a', 'option_8_b', 'option_8_c', 'option_8_d'
                 'question_9', 'option_9_a', 'option_9_b', 'option_9_c', 'option_9_d'
                 'question_10', 'option_10_a', 'option_10_b', 'option_10_c', 'option_10_d'      
            ] 
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
    def test_func(self):
        test = self.get_object()
        if self.request.user == test.teacher:
            return True
        return False
class MCQ10TestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MCQ10TestQuestion
    template_name = 'tester/update.html'
    fields = ['test_name','test_key',
                 'question_1', 'option_1_a', 'option_1_b', 'option_1_c', 'option_1_d'
                 'question_2', 'option_2_a', 'option_2_b', 'option_2_c', 'option_2_d'
                 'question_3', 'option_3_a', 'option_3_b', 'option_3_c', 'option_3_d'
                 'question_4', 'option_4_a', 'option_4_b', 'option_4_c', 'option_4_d'
                 'question_5', 'option_5_a', 'option_5_b', 'option_5_c', 'option_5_d'
                 'question_6', 'option_6_a', 'option_6_b', 'option_6_c', 'option_6_d'
                 'question_7', 'option_7_a', 'option_7_b', 'option_7_c', 'option_7_d'
                 'question_8', 'option_8_a', 'option_8_b', 'option_8_c', 'option_8_d'
                 'question_9', 'option_9_a', 'option_9_b', 'option_9_c', 'option_9_d'
                 'question_10', 'option_10_a', 'option_10_b', 'option_10_c', 'option_10_d'      
            ] 
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
    def test_func(self):
        test = self.get_object()
        if self.request.user == test.teacher:
            return True
        return False
class MCQ10TestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MCQ10TestQuestion
    template_name = 'tester/delete.html'
    success_url = '/'
    def test_func(self):
        test = self.get_object()
        if self.request.user == test.teacher:
            return True
        return False

##########################################################################################################
##########################################################################################################

class MCQ25TestCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MCQ25TestQuestion
    template_name = 'tester/create.html'
    fields = ['test_name','test_key',
                 'question_1', 'option_1_a', 'option_1_b', 'option_1_c', 'option_1_d'
                 'question_2', 'option_2_a', 'option_2_b', 'option_2_c', 'option_2_d'
                 'question_3', 'option_3_a', 'option_3_b', 'option_3_c', 'option_3_d'
                 'question_4', 'option_4_a', 'option_4_b', 'option_4_c', 'option_4_d'
                 'question_5', 'option_5_a', 'option_5_b', 'option_5_c', 'option_5_d'
                 'question_6', 'option_6_a', 'option_6_b', 'option_6_c', 'option_6_d'
                 'question_7', 'option_7_a', 'option_7_b', 'option_7_c', 'option_7_d'
                 'question_8', 'option_8_a', 'option_8_b', 'option_8_c', 'option_8_d'
                 'question_9', 'option_9_a', 'option_9_b', 'option_9_c', 'option_9_d'
                 'question_10', 'option_10_a', 'option_10_b', 'option_10_c', 'option_10_d'
                 'question_11', 'option_11_a', 'option_11_b', 'option_11_c', 'option_11_d'
                 'question_12', 'option_12_a', 'option_12_b', 'option_12_c', 'option_12_d'
                 'question_13', 'option_13_a', 'option_13_b', 'option_13_c', 'option_13_d'
                 'question_14', 'option_14_a', 'option_14_b', 'option_14_c', 'option_14_d'
                 'question_15', 'option_15_a', 'option_15_b', 'option_15_c', 'option_15_d'
                 'question_16', 'option_16_a', 'option_16_b', 'option_16_c', 'option_16_d'
                 'question_17', 'option_17_a', 'option_17_b', 'option_17_c', 'option_17_d'
                 'question_18', 'option_18_a', 'option_18_b', 'option_18_c', 'option_18_d'
                 'question_19', 'option_19_a', 'option_19_b', 'option_19_c', 'option_19_d'
                 'question_20', 'option_20_a', 'option_20_b', 'option_20_c', 'option_20_d'
                 'question_21', 'option_21_a', 'option_21_b', 'option_21_c', 'option_21_d'
                 'question_22', 'option_22_a', 'option_22_b', 'option_22_c', 'option_22_d'
                 'question_23', 'option_23_a', 'option_23_b', 'option_23_c', 'option_23_d'
                 'question_24', 'option_24_a', 'option_24_b', 'option_24_c', 'option_24_d'
                 'question_25', 'option_25_a', 'option_25_b', 'option_25_c', 'option_25_d'    
            ] 
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
    def test_func(self):
        test = self.get_object()
        if self.request.user == test.teacher:
            return True
        return False
class MCQ25TestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MCQ25TestQuestion
    template_name = 'tester/update.html'
    fields = ['test_name','test_key',
                 'question_1', 'option_1_a', 'option_1_b', 'option_1_c', 'option_1_d'
                 'question_2', 'option_2_a', 'option_2_b', 'option_2_c', 'option_2_d'
                 'question_3', 'option_3_a', 'option_3_b', 'option_3_c', 'option_3_d'
                 'question_4', 'option_4_a', 'option_4_b', 'option_4_c', 'option_4_d'
                 'question_5', 'option_5_a', 'option_5_b', 'option_5_c', 'option_5_d'
                 'question_6', 'option_6_a', 'option_6_b', 'option_6_c', 'option_6_d'
                 'question_7', 'option_7_a', 'option_7_b', 'option_7_c', 'option_7_d'
                 'question_8', 'option_8_a', 'option_8_b', 'option_8_c', 'option_8_d'
                 'question_9', 'option_9_a', 'option_9_b', 'option_9_c', 'option_9_d'
                 'question_10', 'option_10_a', 'option_10_b', 'option_10_c', 'option_10_d'
                 'question_11', 'option_11_a', 'option_11_b', 'option_11_c', 'option_11_d'
                 'question_12', 'option_12_a', 'option_12_b', 'option_12_c', 'option_12_d'
                 'question_13', 'option_13_a', 'option_13_b', 'option_13_c', 'option_13_d'
                 'question_14', 'option_14_a', 'option_14_b', 'option_14_c', 'option_14_d'
                 'question_15', 'option_15_a', 'option_15_b', 'option_15_c', 'option_15_d'
                 'question_16', 'option_16_a', 'option_16_b', 'option_16_c', 'option_16_d'
                 'question_17', 'option_17_a', 'option_17_b', 'option_17_c', 'option_17_d'
                 'question_18', 'option_18_a', 'option_18_b', 'option_18_c', 'option_18_d'
                 'question_19', 'option_19_a', 'option_19_b', 'option_19_c', 'option_19_d'
                 'question_20', 'option_20_a', 'option_20_b', 'option_20_c', 'option_20_d'
                 'question_21', 'option_21_a', 'option_21_b', 'option_21_c', 'option_21_d'
                 'question_22', 'option_22_a', 'option_22_b', 'option_22_c', 'option_22_d'
                 'question_23', 'option_23_a', 'option_23_b', 'option_23_c', 'option_23_d'
                 'question_24', 'option_24_a', 'option_24_b', 'option_24_c', 'option_24_d'
                 'question_25', 'option_25_a', 'option_25_b', 'option_25_c', 'option_25_d'      
            ] 
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
    def test_func(self):
        test = self.get_object()
        if self.request.user == test.teacher:
            return True
        return False
class MCQ25TestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MCQ25TestQuestion
    template_name = 'tester/delete.html'
    success_url = '/'
    def test_func(self):
        test = self.get_object()
        if self.request.user == test.teacher:
            return True
        return False

##########################################################################################################
##########################################################################################################


class QnA10TestCreateView(LoginRequiredMixin,  CreateView):
    model = QuestionAndAnsweer10TestQuestion
    template_name = 'tester/cre.html'
    fields = ['test_name','test_key',
                 'question_1',
                 'question_2',
                 'question_3',
                 'question_4',
                 'question_5',
                 'question_6',
                 'question_7',
                 'question_8',
                 'question_9',
                 'question_10',      
            ] 
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
    # def test_func(self):
    #     test = self.get_object()
    #     if self.request.user == test.teacher:
    #         return True UserPassesTestMixin
    #     return False
class QnATestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = QuestionAndAnsweer10TestQuestion
    fields = ['test_name','test_key',
                 'question_1',
                 'question_2',
                 'question_3',
                 'question_4',
                 'question_5',
                 'question_6',
                 'question_7',
                 'question_8',
                 'question_9',
                 'question_10',
            ] 
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
    def test_func(self):
        test = self.get_object()
        if self.request.user == test.teacher:
            return True
        return False
class QnATestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = QuestionAndAnsweer10TestQuestion
    template_name = 'tester/delete.html'
    success_url = '/'
    def test_func(self):
        test = self.get_object()
        if self.request.user == test.teacher:
            return True
        return False