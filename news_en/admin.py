from django.contrib import admin
from .models import EnglishNews

@admin.register(EnglishNews)
class EnglishNewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    