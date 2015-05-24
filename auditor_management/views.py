from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the auditor_management index.")
    return render(request, 'auditor_management/signup.html')


def signup(request):
    return render(request, 'auditor_management/signup.html')
