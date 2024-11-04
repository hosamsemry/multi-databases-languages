from rest_framework import serializers
from .models import FrenchNews

class FrenchNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrenchNews
        fields = ['central_id','media_id', 'title', 'content']