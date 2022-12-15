from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    cover = models.FileField(upload_to='cover_pic/')
    tag = models.ManyToManyField(Tag)
    github = models.URLField(max_length=100)
    live_demo = models.URLField(max_length=60, null=True, blank=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title
   
