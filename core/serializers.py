# core/serializers.py

from rest_framework import serializers
from .models import CentralizedNews, Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file_path', 'created_at']

class CentralizedNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralizedNews
        fields = ['id', 'created_at', 'updated_at']
