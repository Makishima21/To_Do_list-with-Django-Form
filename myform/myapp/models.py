from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):
    USER=[
        ('user','USER'),
        ('admin','Admin'),
    ]
    city=models.CharField(max_length=150,null=True)
    profile_pic=models.ImageField(max_length=150,null=True)
    date_of_birth=models.DateField(null=True)
    
class CategoryModel(models.Model):
    user=models.ForeignKey(customUser,on_delete=models.CASCADE,null=True)
    categoryName=models.CharField(max_length=150,null=True)
    
class TaskModel(models.Model):
    category=models.ForeignKey(CategoryModel, on_delete=models.CASCADE,null=True)
    TaskName=models.CharField(max_length=150,null=True)
    taskdate=models.DateField(max_length=150,null=True)
    