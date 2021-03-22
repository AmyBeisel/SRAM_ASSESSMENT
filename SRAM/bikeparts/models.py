from django.db import models


class Bike(models.Model):
    brand = models.TextField(max_length=200)
    bike_type = models.TextField(max_length=20)
    weight = models.IntegerField()

# class Front_Wheel(models.Model):
#     brand = models.TextField(_(max_length = 200))
#     size = models.TextField(_(max_lenth= 10))
#     weight = models.IntegerField()
    
# class Rear_Wheel(models.Model):
#     brand = models.TextField(_(max_length = 200))
#     size = models.TextField(_(max_lenth= 10))
#     weight = models.IntegerField()


