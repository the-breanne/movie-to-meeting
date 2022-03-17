
# Register your models here.
from django.contrib import admin
from .models import Meeting

class MeetingList(admin.ModelAdmin):
    list_display = ('name', 'date', 'description')
    list_filter = ('name', 'date')
    search_fields = ('name', 'description')
    ordering = ['name']


admin.site.register(Meeting, MeetingList)
