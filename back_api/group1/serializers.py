from .models import Group1
from rest_framework import serializers


class Group1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group1
        fields = ['id', 'name']
