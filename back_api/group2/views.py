from django.shortcuts import render

# Create your views here.
from group2.models import Group2
from rest_framework import viewsets
from rest_framework import permissions
from group2.serializers import Group2Serializer


class Group2ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group2 to be viewed or edited.
    """
    queryset = Group2.objects.all()
    serializer_class = Group2Serializer
    permission_classes = [permissions.IsAuthenticated]  #     AllowAny
                                                        #     IsAuthenticated
                                                        #     IsAdminUser
                                                        #     IsAuthenticatedOrReadOnly

