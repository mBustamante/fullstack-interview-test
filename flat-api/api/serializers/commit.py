
from rest_framework import serializers

from api.serializers.author import AuthorSerializer


class CommitListSerializer(serializers.Serializer):
    author = AuthorSerializer()
    timestamp = serializers.SerializerMethodField()
    message = serializers.CharField()
    hexsha = serializers.CharField()

    def get_timestamp(self, obj):
        return obj.committed_datetime


class CommitDetailSerializer(CommitListSerializer):
    files_afected = serializers.SerializerMethodField()

    def get_files_afected(self, obj):
        return len(obj.stats.files)
