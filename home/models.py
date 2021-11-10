from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    content=models.TextField()
    date= models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "Message from "+ self.name
class Subscribe(models.Model):
    sno=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    def __str__(self):
        return self.name+ "Subscribed"

class Vote(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    cheap=models.CharField(max_length=255)
    badelog=models.CharField(max_length=255)
    randirona=models.CharField(max_length=255)
    active=models.CharField(max_length=255)
    fodu=models.CharField(max_length=255,default='0')
    gaddar=models.CharField(max_length=255,default='0')
    gmg=models.CharField(max_length=255,default='0')
    nakre=models.CharField(max_length=255,default='0')    
    def __str__(self):
        return self.name + " Voted"
        
    
