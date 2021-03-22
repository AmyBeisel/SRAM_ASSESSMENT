from django.db import models


class Bike(models.Model):
    brand = models.TextField(max_length=200)
    bike_type = models.TextField(max_length=20)
    weight = models.IntegerField()

class FrontWheel(models.Model):
    brand = models.TextField(max_length = 200)
    size = models.TextField(max_length= 10)
    weight = models.IntegerField()
    
class RearWheel(models.Model):
    brand = models.TextField(max_length = 200)
    size = models.TextField(max_length= 10)
    weight = models.IntegerField()


