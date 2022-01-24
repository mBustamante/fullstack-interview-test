
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response

from api.mixins import APIView
from api.serializers.branch import BranchSerializer


class BranchView(APIView, generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        return None

    def list(self, request, *args, **kwargs):
        repo = settings.REPO

        serializer = self.get_serializer(repo.branches, many=True)
        return Response(serializer.data)
