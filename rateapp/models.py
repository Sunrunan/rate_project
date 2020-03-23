from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
# Create your models here.
class Module(models.Model):

 Code = models.CharField(max_length = 200)
 Name = models.CharField(max_length = 200)
 Year = models.IntegerField(default=2016)
 Semester = models.IntegerField(default=1)
 Taught_by = models.CharField(max_length=200,default='none')
 def __str__(self):
  return self.Name+" "+str(self.Semester)

class Professor(models.Model):
 Code = models.CharField(max_length=200)
 Name = models.CharField(max_length=200)
 def __str__(self):
  return self.Code+","+self.Name

class RateInfo(models.Model):
 Name = models.CharField(max_length=200,default='a')
 Professor = models.CharField(max_length=200,default='a')
 Year = models.IntegerField(default=2016)
 Semester = models.IntegerField(default=1)
 Rate = models.IntegerField(default=1)
 User = models.CharField(max_length=200,default='a')
 def __str__(self):
  return self.Name

class Results(models.Model):
 Name = models.CharField(max_length=200)
 Rate = models.IntegerField()
 def __str__(self):
  return self.Name


'''class CustomUser(AbstractUser):

 name = models.CharField(max_length=200, null=True, blank=True)'''
