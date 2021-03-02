from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=50)
    movie_startdate = models.DateTimeField()
    movie_enddate = models.DateTimeField()

    def __str__(self):
        return self.movie_name