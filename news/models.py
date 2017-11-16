from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    autor = models.CharField(max_length=32)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    autor = models.CharField(max_length=32)
    content = models.TextField()
    comment_date = models.DateTimeField('date published')
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return 'Author: ' + str(self.autor) + ' Comment: ' + str(self.content)[0:20]
