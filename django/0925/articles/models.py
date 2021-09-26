from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Article(models.Model):
    title = CharField(max_length=50)
    context = TextField()
    img = ImageField(blank=True, upload_to='%Y/%m/%d')
    
    def __str__(self):
        return self.title