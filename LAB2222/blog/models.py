from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    games_won = models.IntegerField(default=0)
    games_lost = models.IntegerField(default=0)
    conference = models.CharField(max_length=100, default='Unknown')
    standing = models.IntegerField()

    def __str__(self):
        return f"{self.city} {self.name}"


class Player(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    position = models.CharField(max_length=100, default='Unknown')
    city = models.CharField(max_length=100, default='Unknown')
    height = models.CharField(max_length=100, default='Unknown')
    weight = models.CharField(max_length=100, default='Unknown')
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
