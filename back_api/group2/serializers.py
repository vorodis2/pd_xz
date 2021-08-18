from .models import Group2
from rest_framework import serializers


class Group2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group2
        fields = ['id', 'name']
