from django import forms
from .models import ReminderModel
from django.contrib.admin import widgets

class ReminderForm(forms.ModelForm):

    set_for = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    class Meta:

        model = ReminderModel
        fields = '__all__'