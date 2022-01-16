from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, login as django_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  

# Create your views here.
def signup(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

        else:

            for msg in form.error_messages:
                    
                print(form.error_messages[msg])

    else:

        form = CustomUserCreationForm()

    context = {
        'form' : form
    }

    return render(request, 'users/signup.html', context)


def login(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)

            return redirect('app')

    else:

        form = AuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'users/login.html', context)

def logout(request):

    django_logout(request)

    return redirect('home')