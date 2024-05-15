from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Question(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(default=timezone.now)
    name = models.CharField('Name', max_length=50, null=True, blank=True)
    content = models.TextField('Content', unique=True)
    hashtag=models.ManyToManyField(HashTag)
    ##좋아요 기능을 위한 추가
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True, blank=True)
    like = models.ManyToManyField(User, related_name='likes', blank = True)
    def __str__(self):
        return 'id : {}, title : {}' .format(self.id, self.title, self.contents)
    

    def __str__(self): 
        return self.title
    
class Comment(models.Model):
    question=models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text
