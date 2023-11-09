from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=30)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    