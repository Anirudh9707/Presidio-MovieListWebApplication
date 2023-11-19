from django.db import models

# Create your models here.
class Movies(models.Model):
    moviename=models.CharField(max_length=255)
    direcname=models.CharField(max_length=255)
    language=models.CharField(max_length=255)
    year=models.IntegerField()
    rating=models.IntegerField(default=0)
    poster = models.ImageField(upload_to='posters/', default='default_poster.jpg')