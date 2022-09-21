from rest_framework import serializers
from CPLN.models import *


class UserPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userpage
        fields = ('username', 'password')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class DailyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCard
        fields = '__all__'
