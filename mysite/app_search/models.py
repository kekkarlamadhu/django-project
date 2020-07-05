from django.db import models

# Create your models here.
from datetime import datetime,date
from django.contrib.auth.models import User


APP_CATEGORIES = (
    ('GOOGLE', 'google play store'),
    ('APPLE', 'apple play store'),

)
class AppInfo(models.Model):
    app_type = models.CharField(max_length=100,choices=APP_CATEGORIES)
    app_name= models.CharField(max_length=50)
    app_icon = models.ImageField(upload_to='images/')
    developer_name= models.CharField(max_length=50)
    no_of_downloads = models.CharField(max_length=50)
    app_rating = models.CharField(max_length=50)
    no_of_reviews= models.CharField(max_length=50)
    description=models.TextField(max_length=200)

    def __str__(self):
        return self.app_name

class KeyWordData(models.Model):
    app_category= models.ForeignKey(AppInfo, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    url=models.URLField(max_length=200)