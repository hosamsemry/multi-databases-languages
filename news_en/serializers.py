from rest_framework import serializers
from .models import EnglishNews

class EnglishNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishNews
        fields = ['central_id','media_id','title', 'content']