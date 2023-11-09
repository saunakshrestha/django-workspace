from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30,null=True)
    body = models.TextField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

