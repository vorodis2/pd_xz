from apps.group.models import (
    Group,
    GroupFile, GroupSort,GroupComment, MODEL_NAME,
)
from src.base_view_set import BaseViewSet, BaseFileViewSet, BaseSortViewSet,BaseCommentViewSet
from .serializers import (
    GroupSerializer,
    GroupFileSerializer, GroupSortSerializer, GroupSmallSerializer,GroupCommentSerializer
)
from api.utils import get_counter_response_from_file


class GroupViewSet(BaseViewSet):

    """
    Представление для Group модели.
    """
    ObjectClass = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    file_serializer_class = GroupFileSerializer
    OBJECTS_FILENAME = 'group.json'


class GroupFileViewSet(BaseFileViewSet):
    """
    Представление для GroupFile модели.
    """
    
    ObjectClass = GroupFile
    queryset = GroupFile.objects.all()
    serializer_class = GroupFileSerializer


class GroupSortViewSet(BaseSortViewSet):
    """
    Представление для GroupSort модели.
    """
    queryset = GroupSort.objects.all()
    serializer_class = GroupSortSerializer


class GroupCommentViewSet(BaseCommentViewSet):
    """
    Представление для GroupSort модели.
    """
    queryset = GroupComment.objects.all()
    serializer_class = GroupCommentSerializer



def get_last_change_time(request, *args, **kwargs):
    return get_counter_response_from_file(got_model_instance=eval(MODEL_NAME))


class GroupSmallViewSet(BaseViewSet):
    ObjectClass = Group
    queryset = Group.objects.all()
    serializer_class = GroupSmallSerializer
    file_serializer_class = GroupFileSerializer
    OBJECTS_FILENAME = 'group.json'

    # 'sort', Sort is used to retrieve multiple values in list method
    filterset_fields = ("name", "id", 'up', 'name', 'user', 'public')  #

    # filterset_class = MultipleValuesFilterSet

    # permission_classes_by_action = {
    #     "list": (
    #         IsAuthenticatedOrReadOnly,
    #     ),
    #     'retrieve': (
    #         IsAuthenticated and IsUsersObjectOrAdmin,
    #     ),
    #     "create": (
    #         IsAuthenticated,
    #     ),
    #     "update": (
    #         IsAuthenticated and IsUsersObjectOrAdmin,
    #     ),
    #     "partial_update": (
    #         IsAuthenticated and IsUsersObjectOrAdmin,
    #     ),
    #     "destroy": (
    #         IsAuthenticated and IsUsersObjectOrAdmin,
    #     ),
    #     'default': (
    #         IsAuthenticatedOrReadOnly,
    #     ),
    # }

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()

    #     sort_values = self.request.query_params.get('sort', None)
    #     if sort_values:
    #         sort_list = sort_values.split(',')
    #         queryset = queryset.filter(sort__in=sort_list)

    #     queryset = self.filter_queryset(queryset)[::-1]

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def get_permissions(self):
    #     try:
    #         # return permission_classes depending on `action`
    #         return [permission() for permission in self.permission_classes_by_action[self.action]]
    #     except KeyError:
    #         # action is not set return default permission_classes
    #         return [permission() for permission in self.permission_classes_by_action['default']]

    """
    Retrieve a model instance.
    """
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)