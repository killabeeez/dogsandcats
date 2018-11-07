from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pets

class PetsViewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Pets
        fields = ('id', 'owner', 'name', 'birthday')
