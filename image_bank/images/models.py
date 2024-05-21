from django.db import models
import os
from storages.backends.azure_storage import AzureStorage
from uuid import uuid4


def upload_to(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = f"{uuid4()}.{extension}"
    return os.path.join('images', new_filename)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/', storage=AzureStorage())
    original_name = models.CharField(max_length=255)
    generated_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.original_name
