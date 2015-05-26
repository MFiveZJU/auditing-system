from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from auditor_management.forms.auditor_signup_form import AuditorSignupForm
# from auditor_management.forms import NameForm

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the auditor_management index.")
    return render(request, 'auditor_management/signup.html')


def signup(request):
    if request.method == 'POST':
        form = AuditorSignupForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/auditor_management/test/')
    else:
        form = AuditorSignupForm()
    return render(request, 'auditor_management/signup.html', {'form': form})


def test(request):
    return HttpResponse("test succeed.")
