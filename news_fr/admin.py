from django.contrib import admin
from .models import FrenchNews



@admin.register(FrenchNews)
class FrenchNewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
