from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from auditor_management.forms.auditor_signup_form import AuditorSignupForm
from auditor_management.forms.auditor_signin_form import AuditorSigninForm


def index(request):
    # return HttpResponse("Hello, world. You're at the auditor_management index.")
    return render(request, 'auditor_management/signin.html', {'form': AuditorSigninForm()})


def signup(request):
    if request.method == 'POST':
        form = AuditorSignupForm(request.POST)
        if form.is_valid():
            auditor_signup()
            return HttpResponseRedirect('/auditor_management/test/')
    else:
        form = AuditorSignupForm()
    return render(request, 'auditor_management/signup.html', {'form': form})


def auditor_signup(request):
    a = 5

# request.POST['foobar']
# if (Auditor().)

def signin(request):
    if request.method == 'POST':
        form = AuditorSigninForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/auditor_management/test/')
    else:
        form = AuditorSigninForm()
    return render(request, 'auditor_management/signin.html', {'form': form})


def test(request):
    return HttpResponse("test succeed.")
