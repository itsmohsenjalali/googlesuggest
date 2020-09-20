from django.contrib import admin
from .models import Suggestion, Word
# Register your models here.


class WordAdmin(admin.ModelAdmin):
    list_display = ('key', 'word')


class SuggestAdmin(admin.ModelAdmin):
    list_display = ('word', 'sugg')


admin.site.register(Suggestion, SuggestAdmin)
admin.site.register(Word, WordAdmin)
