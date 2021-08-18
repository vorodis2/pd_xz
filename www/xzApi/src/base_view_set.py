import os
import json

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from planback.settings import NON_AUTHENTICATED_API_ACCESS
from src.base_serializer import (
    BaseSerializer,
    BaseFileSerializer,
)
from src.base_object import BaseObject


class BaseViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    """
    Представление для Базовой модели.
    Для наследования стоит переопределить поля: ObjectClass,
                                                queryset,
                                                serializer_class,
                                                file_serializer_class,
                                                OBJECTS_FILENAME,
    """

    class Meta:
        abstract = True

    permission_classes = (NON_AUTHENTICATED_API_ACCESS,)
    permission_classes_by_action = {'list_me': (IsAuthenticated,)}
    ObjectClass = BaseObject
    serializer_class = BaseSerializer
    file_serializer_class = BaseFileSerializer
    OBJECTS_FILENAME = 'base.json'
    COMMON_FILENAME = 'common.json'
    COUNTER = "counter"

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('up', 'name', 'user', 'sort', 'id',)

    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())[::-1]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list_me(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user.pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if hasattr(request.data, '_mutable'):
                last_mutable = request.data._mutable
                request.data._mutable = True
                request.data['user'] = request.user.pk
                request.data._mutable = last_mutable
            else:
                request.data['user'] = request.user.pk

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def export(self, request):
        json_objects_filename = self.OBJECTS_FILENAME
        json_common_filename = self.COMMON_FILENAME

        json_objects_filepath = settings.MEDIA_ROOT / 'json' / json_objects_filename  # noqa: E501
        json_common_filepath = settings.MEDIA_ROOT / 'json' / json_common_filename  # noqa: E501

        json_objects_data = []
        json_common_data = {}

        for model_object in self.queryset:
            json_objects_data.append({
                'id': model_object.pk,
                'user': model_object.user,
                'name': model_object.name,
                'files': self.file_serializer_class(model_object.files.all(),
                                                    many=True,
                                                    read_only=True).data,
            })

        if not os.path.exists(settings.MEDIA_ROOT / 'json'):
            os.makedirs(settings.MEDIA_ROOT / 'json')

        if os.path.isfile(json_common_filepath):
            with open(json_common_filepath, 'r') as f:
                json_common_data = json.loads(f.read())

                if self.COUNTER in json_common_data:
                    json_common_data[self.COUNTER] += 1
                else:
                    json_common_data[self.COUNTER] = 0
        else:
            json_common_data[self.COUNTER] = 0

        with open(json_objects_filepath, 'w+') as f:  # noqa: E501
            json.dump(json_objects_data, f)

        with open(json_common_filepath, 'w+') as f:  # noqa: E501
            json.dump(json_common_data, f)

        return Response({
            'file_url': request.build_absolute_uri(
                f'{settings.MEDIA_URL}json/{json_objects_filename}'
            ),
            self.COUNTER: json_common_data[self.COUNTER],
        }, status=status.HTTP_201_CREATED)


class BaseFileViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Представление для Файла базовой модели.
    Для наследования стоит переопределить поля: ObjectClass,
                                                queryset,
                                                serializer_class,
    """
    class Meta:
        abstract = True

    permission_classes = (NON_AUTHENTICATED_API_ACCESS,)
    # ObjectClass = BaseObjectFile                  # Warning:  Will not allow to compile
    # queryset = BaseObjectFile.objects.all()       # Warning:  Will not allow to compile
    serializer_class = BaseFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        https_serializer_data = dict(serializer.data)

        if https_serializer_data['src'].startswith('http://'):
            https_serializer_data['src'] = https_serializer_data['src'].replace('http://', 'https://')

        return Response(https_serializer_data, status=status.HTTP_201_CREATED, headers=headers)


class BaseSortViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Представление для объекта Sort базовой модели.
    Для наследования стоит переопределить поля: ObjectClass,
                                                queryset,
                                                serializer_class,
    """
    class Meta:
        abstract = True

    permission_classes = [NON_AUTHENTICATED_API_ACCESS]
