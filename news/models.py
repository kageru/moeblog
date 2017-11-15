from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    autor = models.CharField(max_length=32)
    description = models.TextField()
    content = models.TextField()

