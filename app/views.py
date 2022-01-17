from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import context
from app.forms import ReminderForm
from .models import ReminderModel
import requests

# Create your views here.
def home(request):

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers)

    response = response.json()

    context = {
        'quote' : response
    }

    return render(request, 'home.html', context)

@login_required(login_url='login')
def app(request):

    current_user = request.user

    reminder_all = ReminderModel.objects.filter(status=0, user=current_user).order_by('-updated_on')

    reminder_all_count = len(ReminderModel.objects.filter(status=0, user=current_user))

    complete_all = ReminderModel.objects.filter(status=1, user=current_user).order_by('-updated_on')

    complete_all_count = len(ReminderModel.objects.filter(status=1, user=current_user))

    tag_priority = ReminderModel.objects.filter(status=0, tag='priority', user=current_user).order_by('-updated_on')

    tag_priority_count = len(ReminderModel.objects.filter(status=0, tag='priority', user=current_user))

    tag_work = ReminderModel.objects.filter(status=0, tag='work', user=current_user).order_by('-updated_on')

    tag_work_count = len(ReminderModel.objects.filter(status=0, tag='work', user=current_user))

    tag_home = ReminderModel.objects.filter(status=0, tag='home', user=current_user).order_by('-updated_on')

    tag_home_count = len(ReminderModel.objects.filter(status=0, tag='home', user=current_user))

    tag_family = ReminderModel.objects.filter(status=0, tag='family', user=current_user).order_by('-updated_on')

    tag_family_count = len(ReminderModel.objects.filter(status=0, tag='family', user=current_user))

    tag_leisure = ReminderModel.objects.filter(status=0, tag='leisure', user=current_user).order_by('-updated_on')

    tag_leisure_count = len(ReminderModel.objects.filter(status=0, tag='leisure', user=current_user))

    context = {
        'all' : reminder_all,
        'all_count' : reminder_all_count,
        'complete' : complete_all,
        'complete_count' : complete_all_count,
        'priority' : tag_priority,
        'priority_count' : tag_priority_count,
        'work' : tag_work,
        'work_count' : tag_work_count,
        'home': tag_home,
        'home_count' : tag_home_count,
        'family': tag_family,
        'family_count' : tag_family_count,
        'leisure' : tag_leisure,
        'leisure_count' : tag_leisure_count,
        'current_user' : current_user
    }

    return render(request, 'app/index.html', context)

@login_required(login_url='login')
def upload(request):

    current_user = request.user

    if request.method == 'POST':

        form = ReminderForm(request.POST)

        if form.is_valid():

            form.save()
            
        return redirect('app')

    else:
        form = ReminderForm()

    context = {
        'form' : form,
        'current_user' : current_user
    }

    return render(request, 'app/upload.html', context)

def done(request, id):

    reminder_obj = ReminderModel.objects.filter(id=id).update(status=1)

    return redirect('app')

def delete(request, id):

    reminder_obj = ReminderModel.objects.filter(id=id)

    reminder_obj.delete()

    return redirect('app')