from django.db import models

# Create your models here.
class Exercise(models.Model):
    
    bodypart = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    cover_img = models.ImageField(null=True, blank=True, default="no_img.gif")
    name = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    difficulty = models.CharField(null=True, blank=True, max_length=50)
    
    def __str__(self):
        return self.name