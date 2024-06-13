from django.db import models
from django.contrib.auth.models import User


class Directory(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Публичный'),
        (PRIVATE, 'Приватный'),
    ]

    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subdirectories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="directory_images/", null=True, blank=True, default='images/default.jpg')
    user = models.ForeignKey(User, related_name='directories', on_delete=models.CASCADE)
    author = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=7, choices=VISIBILITY_CHOICES, default=PUBLIC)

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    directory = models.ForeignKey(Directory, related_name='records', on_delete=models.CASCADE, blank=False, null=False)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)
    author = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=7, choices=Directory.VISIBILITY_CHOICES, default=Directory.PUBLIC)

    def __str__(self):
        return self.title