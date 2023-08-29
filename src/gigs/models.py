from django.db import models
from django.contrib.postgres.fields import ArrayField

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='artists/', null=True, blank=True)
    contact_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Production(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    lineup = models.ManyToManyField(Artist)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    
    def __str__(self):
        return self.name