from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from bikeparts.models import Bike

# # Serializers define the API representation.
# class QuestionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta: 
#         model = Question 
#         fields = ['question_text', 'pub_date']

# # ViewSets define the view behavior.
# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# Serializers define the API representation.
class BikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Bike 
        fields = ['brand', 'bike_type', 'weight']

# ViewSets define the view behavior.
class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'Questions', QuestionViewSet)
router.register(r'Bikes', BikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('rest_framework.urls')),
    path('bikeparts/', include('bikeparts.urls')),
    path('admin/', admin.site.urls),
]


