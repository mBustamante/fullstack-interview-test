
from django.conf import settings
from rest_framework import serializers

from app.prs.models import PullRequest


class PullRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PullRequest
        fields = ('title', 'description', 'source', 'target',
                  'status',)

    def create(self, validated_data):
        if validated_data['status'] == PullRequest.CLOSED_STATUS:
            raise serializers.ValidationError('Invalid status')

        pr = PullRequest(**validated_data)
        pr.author_name = settings.REPO_AUTHOR_NAME
        pr.author_email = settings.REPO_AUTHOR_EMAIL
        if pr.status == PullRequest.MERGED_STATUS:
            try:
                pr.merge()
            except Exception:
                raise serializers.ValidationError('Conflicts on merge')
        pr.save()
        return pr
