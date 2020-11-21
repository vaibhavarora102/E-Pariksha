from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tester/index.html')
def about(request):
    return render(request, 'tester/about.html')
def contact(request):
    return render(request, 'tester/contact.html')