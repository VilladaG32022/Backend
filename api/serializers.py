from rest_framework import serializers
from CPLN.models import *
from django.contrib.admin.models import LogEntry

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'

class ListFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListFood
        fields = '__all__'