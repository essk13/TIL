from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.files import ImageField
from imagekit import processors
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = CharField(max_length=100)
    content = TextField()
    image = ImageField(blank=True, upload_to='%Y/%m/%d')
    img_thumb = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 200)],
        format='PNG',
        options={
            'quality':90,
        }
    )
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title