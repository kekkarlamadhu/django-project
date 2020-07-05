
from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class UserData(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    profile_image=models.ImageField(default='logo6.png',upload_to='profile_image/',null=True,blank=True)


    def __str__(self):
        return self.user.username
