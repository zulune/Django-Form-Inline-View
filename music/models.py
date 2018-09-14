from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s" % (self.number, self.name)

    class Meta:
        unique_together = ('album', 'number', 'name', )