# Generated by Django 3.2.25 on 2024-05-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_question_likes_count_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='community_photo'),
        ),
    ]
