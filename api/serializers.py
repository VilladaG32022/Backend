from rest_framework import serializers
from CPLN.models import *


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ListFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListFood
        fields = '__all__'

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'