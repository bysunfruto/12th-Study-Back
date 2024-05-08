from django.contrib import admin
from community.models import Question, Comment, HashTag, Like

# Register your models here.

admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(HashTag)
admin.site.register(Like)