from django.shortcuts import render

# Create your views here.
from group1.models import Group1
from rest_framework import viewsets
from rest_framework import permissions
from group1.serializers import Group1Serializer


class Group1ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group1 to be viewed or edited.
    """
    queryset = Group1.objects.all()
    serializer_class = Group1Serializer
    permission_classes = [permissions.AllowAny]  #     AllowAny
                                                 #     IsAuthenticated
                                                 #     IsAdminUser
                                                 #     IsAuthenticatedOrReadOnly

