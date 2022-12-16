from django.db import models

# Create your models here.
class Exercise(models.Model):
    
    bodypart = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name