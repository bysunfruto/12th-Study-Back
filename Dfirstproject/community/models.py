from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField('date published')
    content = models.TextField('Content')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]