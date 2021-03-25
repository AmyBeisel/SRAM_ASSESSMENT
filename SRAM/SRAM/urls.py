from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from bikeparts.models import Bike, FrontWheel, RearWheel

# Serializers define the API representation.
class BikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Bike 
        fields = ['id','brand', 'bike_type', 'weight']
# Serializers define the API representation.
class FrontWheelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = FrontWheel 
        fields = ['id','brand', 'size', 'weight']
# Serializers define the API representation.
class RearWheelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = RearWheel 
        fields = ['id', 'brand', 'size', 'weight']

# ViewSets define the view behavior.
class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

# ViewSets define the view behavior.
class FrontWheelViewSet(viewsets.ModelViewSet):
    queryset = FrontWheel.objects.all()
    serializer_class = FrontWheelSerializer

# ViewSets define the view behavior.
class RearWheelViewSet(viewsets.ModelViewSet):
    queryset = RearWheel.objects.all()
    serializer_class = RearWheelSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'Questions', QuestionViewSet)
router.register(r'Bike', BikeViewSet)
router.register(r'FrontWheel', FrontWheelViewSet)
router.register(r'RearWheel', RearWheelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('rest_framework.urls')),
    path('bikeparts/', include('bikeparts.urls')),
    path('admin/', admin.site.urls),
]


