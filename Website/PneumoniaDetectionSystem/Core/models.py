from django.db import models

# Create your models here.

class UploadImage(models.Model):
    image =  models.ImageField(upload_to='uploads/')
    uploadTime = models.DateTimeField(auto_now_add=True)