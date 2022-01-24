
from rest_framework import serializers


class BranchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
