import datetime
from django.db import models
from django.utils import timezone

class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.movie_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class LikeIt(models.Model):
    movie = models.ForeignKey(Movie)
    likeit_text = models.CharField(max_length=200)
    upvote = models.IntegerField(default=0)

    def __str__(self):
    	return self.likeit_text