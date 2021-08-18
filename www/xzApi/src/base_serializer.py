from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для Базовой модели.
    """

    files = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class BaseFileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для Базовой File модели.
    """
    pass
