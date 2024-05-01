from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(default=timezone.now)
    name = models.CharField('Name', max_length=50, blank=True)
    content = models.TextField('Content', unique=True)

    def __str__(self): 
        return self.title
