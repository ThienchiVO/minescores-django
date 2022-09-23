from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)


class Score(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.DurationField()
    height = models.IntegerField()
    length = models.IntegerField()
    mines = models.IntegerField()


class Size(models.Model):
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    length = models.IntegerField()
    mines = models.IntegerField()
