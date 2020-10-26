from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myUser(models.Model):
    user_name=models.CharField(max_length=24,unique=True)

    def __str__(self):
        return self.user_name

class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name
        
class Webpage(models.Model):
    top=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    page=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)

class Client(models.Model):
    user_name=models.CharField(max_length=24,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=24)
    def __str__(self):
        return self.user_name

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username