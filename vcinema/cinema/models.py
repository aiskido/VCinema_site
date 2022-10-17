from django.db import models


# Create your models here.
# class Directory
# class Genre
class Movies(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='movies/%Y', blank=True)
    rating = models.FloatField()
    release_date = models.DateField()
    age_rest = models.IntegerField()
    directory = models.CharField(max_length=100)
    video = models.URLField(max_length=128)
    article = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('release_date',)
        verbose_name_plural = 'Movies'
        verbose_name = 'Movie'


class Comments(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ForeignKey('Movies', on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'