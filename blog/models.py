from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    autor = models.CharField(max_length=32)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    name = models.CharField(max_length=16)

    def __str__(self):
        return 'Post: ' + str(self.article_id) + ' --- Tag: ' + str(self.name)
