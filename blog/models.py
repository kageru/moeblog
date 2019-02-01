from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    htmlname = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Tag(models.Model):
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    name = models.CharField(max_length=16)

    def __str__(self):
        return 'Post: ' + str(self.article_id) + ' --- Tag: ' + str(self.name)

class Author(models.Model):
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.article_id.title + ' - ' + self.name

class Comment(models.Model):
    author = models.CharField(max_length=32)
    content = models.TextField()
    comment_date = models.DateTimeField('date published')
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return 'Author: ' + str(self.author) + ' Comment: ' + str(self.content)[0:20]
