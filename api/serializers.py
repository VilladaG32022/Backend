from rest_framework import serializers
from CPLN.models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class DailyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCard
        fields = '__all__'

class ListFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListFood
        fields = '__all__'

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'