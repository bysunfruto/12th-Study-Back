# Generated by Django 4.2.11 on 2024-03-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Title')),
                ('upload_time', models.DateTimeField(unique=True)),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
    ]
