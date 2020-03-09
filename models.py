from django.db import models


# Create your models here.
class ScrapbookTable(models.Model):
    picture = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=50)
    experience = models.CharField(max_length=5000)




