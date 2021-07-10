from django.db import models

# Create your models here.
class Post(models.Model):
    Name=models.CharField(max_length=100)
    Title=models.CharField(max_length=100)
    Message=models.TextField(max_length=1000)
    dat=models.DateTimeField(auto_now_add=True)