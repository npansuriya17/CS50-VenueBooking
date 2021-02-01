from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Venues(models.Model):
    venue_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    website = models.CharField(max_length=70)
    contact = models.IntegerField()
    
    def __str__(self):
        return '%s %s %s %s' % (self.venue_name, self.address, self.website, self.contact)



class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    
    def __str__(self):
        return '%s' % (self.genre_name)


class Artist(models.Model):
    artist_name = models.CharField(max_length=60)
    music_type = models.ManyToManyField(Genre)
    intro = models.CharField(max_length=500)
    
    def __str__(self):
        return '%s %s %s' % (self.artist_name, str(self.music_type), self.intro)


class Shows(models.Model):
    show_name = models.CharField(max_length=60)
    venue = models.ForeignKey(Venues, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    time = models.CharField(max_length=10)
    date = models.DateField()
    charges = models.IntegerField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.show_name, str(self.venue), str(self.artist), self.time, self.date, self.charges)