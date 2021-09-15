from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.

class Article(models.Model):
    title = CharField(max_length=100)
    content = TextField()
    image = ImageField(blank=True, upload_to='%Y/%m/%d')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title