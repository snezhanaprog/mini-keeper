from django.db import models


class Directory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subdirectories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="directory_images/", null=True, blank=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    directory = models.ForeignKey(Directory, related_name='records', on_delete=models.CASCADE, blank=False, null=False)
    description = models.TextField()

    def __str__(self):
        return self.title