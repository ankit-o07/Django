from django.db import models

# Create your models here.


class Polls(models.Model):
    poll = models.ForeignKey(poll)

class Preson(models.Model):
    SHIRT_SIZES =[
        ("S","Small"),
        ("M","Medium"),
        ("L", "Large"),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument  = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    relesae_date = models.DateField()
    num_stars  = models.IntegerField()

