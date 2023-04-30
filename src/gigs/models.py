from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='artists/', null=True, blank=True)

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

class Location(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Production(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    production = models.ForeignKey(Production, on_delete=models.CASCADE)

    def __str__(self):
        return self.name