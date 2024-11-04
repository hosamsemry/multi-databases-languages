from django.db import models


class CentralizedNews(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Media(models.Model):
    id = models.AutoField(primary_key=True)
    file_path = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)