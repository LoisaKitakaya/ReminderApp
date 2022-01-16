from django.contrib import admin
from .models import ReminderModel

# Register your models here.
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'set_for', 'tag', 'user')
    list_filter = ('status', 'tag')
    search_fields = ['status', 'tags', 'user', 'reminder']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ReminderModel, ReminderAdmin)
