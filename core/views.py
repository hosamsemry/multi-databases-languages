# core/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CentralizedNews, Media
from .serializers import CentralizedNewsSerializer, MediaSerializer
from news_ar.models import ArabicNews
from news_ar.serializers import ArabicNewsSerializer
from news_en.models import EnglishNews
from news_en.serializers import EnglishNewsSerializer
from news_fr.models import FrenchNews
from news_fr.serializers import FrenchNewsSerializer


class NewsDetailView(APIView):
    def get(self, request, news_id, language, format=None):
        try:
            # Fetch from the core news model
            news = CentralizedNews.objects.get(id=news_id)
            core_data = CentralizedNewsSerializer(news).data

            # Fetch the media object using media_id
            if language == 'ar':
                news_detail = ArabicNews.objects.get(central_id=news_id)
                news_data = ArabicNewsSerializer(news_detail).data

            # same for 'en' and 'fr'
            elif language == 'en':
                news_detail = EnglishNews.objects.get(central_id=news_id)
                news_data = EnglishNewsSerializer(news_detail).data

            elif language == 'fr':
                news_detail = FrenchNews.objects.get(central_id=news_id)
                news_data = FrenchNewsSerializer(news_detail).data

            # Fetch media details, if available
            media_id = news_data.get('media_id')
            media_data = None
            if media_id:
                media = Media.objects.get(id=media_id)
                media_data = MediaSerializer(media).data

            response_data = {
                'core': core_data,
                'news': news_data,
                'media': media_data
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except CentralizedNews.DoesNotExist:
            return Response({"error": "news not found"}, status=status.HTTP_404_NOT_FOUND)
