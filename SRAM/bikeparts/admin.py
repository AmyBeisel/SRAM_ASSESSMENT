from django.contrib import admin
from .models import Bike, FrontWheel, RearWheel


admin.site.register(Bike)
admin.site.register(FrontWheel)
admin.site.register(RearWheel)