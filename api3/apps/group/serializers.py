from rest_framework import serializers

from apps.group.models import (
    Group,
    GroupFile, GroupSort, GroupComment
)


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для Group модели.
    """

    files = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'


class GroupFileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для GroupFile модели.
    """

    class Meta:
        model = GroupFile
        fields = '__all__'


class GroupSortSerializer(serializers.ModelSerializer):
    """
    Сериализатор для GroupSort модели.
    """
    
    class Meta:
        model = GroupSort
        fields = '__all__'


class GroupCommentSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = GroupComment
        fields = '__all__'



class GroupSmallSerializer(serializers.ModelSerializer):
    """
    Маленький Сериализатор для Group2 модели.
    """

    # files = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = (
            "id",            
            "name",
            "icon",
            # "ru",
            # "en",
            # 'public',
            # 'up',            
        )
