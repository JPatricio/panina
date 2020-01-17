from django.db import models

from myauth.models import Profile


class Collection(models.Model):
    name = models.CharField(max_length=50)
    # The bonus will be a string, comma separated with the value modifiers for each attribute
    # power,damage,heal
    bonus = models.CharField(max_length=30)


class Card(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    base_power = models.IntegerField()
    base_damage = models.IntegerField()


class UserCollection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    count = models.IntegerField()
