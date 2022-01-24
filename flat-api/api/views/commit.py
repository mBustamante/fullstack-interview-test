
from django.conf import settings
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from api.mixins import APIView
from api.serializers.commit import CommitListSerializer
from api.serializers.commit import CommitDetailSerializer


class CommitListView(APIView, generics.ListAPIView):
    serializer_class = CommitListSerializer

    def list(self, request, *args, **kwargs):
        branch = self.kwargs['branch']
        repo = settings.REPO
        try:
            commits = list(repo.iter_commits(branch, max_count=1000))
        except Exception:
            return Response({'errors': 'Invalid branch'},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(commits, many=True)
        return Response(serializer.data)


class CommitDetailView(APIView, generics.RetrieveAPIView):
    serializer_class = CommitDetailSerializer

    def get(self, request, *args, **kwargs):
        commit_hex = self.kwargs['commit_hex']
        repo = settings.REPO
        try:
            commit = repo.commit(commit_hex)
        except Exception:
            return Response({'errors': 'Invalid commit hex'},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(commit)
        return Response(serializer.data)
