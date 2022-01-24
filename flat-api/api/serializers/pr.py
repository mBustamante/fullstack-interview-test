
from django.conf import settings
from rest_framework import serializers

from app.prs.models import PullRequest


class PullRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PullRequest
        fields = ('title', 'description', 'source', 'target',
                  'status',)

    def validate_source(self, source):
        try:
            settings.REPO.heads[source]
        except IndexError:
            raise serializers.ValidationError('Invalid source branch')
        return source

    def validate_target(self, target):
        try:
            settings.REPO.heads[target]
        except IndexError:
            raise serializers.ValidationError('Invalid target branch')
        return target

    def create(self, validated_data):
        if validated_data['status'] == PullRequest.CLOSED_STATUS:
            raise serializers.ValidationError('Invalid status')

        pr = PullRequest(**validated_data)
        pr.author_name = settings.REPO_AUTHOR_NAME
        pr.author_email = settings.REPO_AUTHOR_EMAIL
        if pr.status == PullRequest.MERGED_STATUS:
            try:
                pr.merge()
            except Exception as e:
                print(e)
                raise serializers.ValidationError('Conflicts on merge')
        pr.save()
        return pr
