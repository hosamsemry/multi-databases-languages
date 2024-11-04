from django.db import models

class FrenchNews(models.Model):
    central_id = models.IntegerField(primary_key='True') 
    media_id = models.IntegerField() 
    title = models.CharField(max_length=255)
    content = models.TextField()