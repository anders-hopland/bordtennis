from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rating = models.IntegerField()
    game = models.ForeignKey(Games, on_delete=models.CASCADE())

    def __str__(self):
        return self.first_name, self.last_name


class Games(models.Model):
    home_player = models.IntegerField()
    away_player = models.IntegerField()
    result = models.CharField()
    winner = models.IntegerField()
    date = models.DateTimeField()



