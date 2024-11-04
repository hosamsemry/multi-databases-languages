from django.contrib import admin
from .models import ArabicNews


@admin.register(ArabicNews)
class ArabicNewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
