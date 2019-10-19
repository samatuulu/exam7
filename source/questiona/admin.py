from django.contrib import admin

from .models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question', 'created_at']
    list_filter = ['question']
    list_display_links = ['pk', 'question']
    search_fields = ['question']
    fields = ['question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'answer']
    list_filter = ['answer']
    list_display_links = ['pk', 'answer']
    search_fields = ['answer']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)