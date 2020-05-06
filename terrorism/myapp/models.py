from django.db import models

# Create your models here.
from django.db import models


class LatestNews(models.Model):
  News_Title = models.CharField(max_length=500,primary_key=True)
  Date = models.DateField(max_length=30)
  Image = models.ImageField(upload_to='pics',blank=True)
  Description = models.TextField(max_length=1024*2)
  def __str__(self):
    return self.News_Title

    
class Agencies(models.Model):
  Agency_Name = models.CharField(max_length=50)
  Image = models.ImageField(upload_to='pics', blank=True)
  Agency_Description = models.TextField(max_length=1024*2)
  Contact_Info = models.BigIntegerField()
  Agency_Address = models.CharField(max_length=500)
  def __str__(self):
    return self.Agency_Name



class MostWantedCriminals(models.Model):
  Criminal_Name=models.CharField(max_length=100)
  Image=models.ImageField(upload_to='pics')
  Description=models.TextField(max_length=1024*2)
  def __str__(self):
         return self.Criminal_Name

class Person(models.Model):
  first_name = models.CharField(max_length=30) 
  last_name = models.CharField(max_length=30)
  def __str__(self):
    return self.first_name



  
 
