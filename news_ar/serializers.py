from rest_framework import serializers
from .models import ArabicNews

class ArabicNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArabicNews
        fields = ['central_id','media_id', 'title', 'content']