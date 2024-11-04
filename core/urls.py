# core/urls.py

from django.urls import path
from .views import NewsDetailView

urlpatterns = [
    path('news/<int:news_id>/<str:language>/', NewsDetailView.as_view(), name='news-detail'),
]
