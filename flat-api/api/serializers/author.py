
from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    email = serializers.CharField(max_length=64)
