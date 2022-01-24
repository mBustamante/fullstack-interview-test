
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from api.mixins import APIView
from api.serializers.pr import PullRequestSerializer
from app.prs.models import PullRequest


class PullRequestView(APIView, generics.ListCreateAPIView):
    serializer_class = PullRequestSerializer

    def get_queryset(self):
        return PullRequest.objects.all()


class PullRequestCloseView(APIView):

    def post(self, request, *args, **kwargs):
        pr_id = self.kwargs['pk']
        pr = get_object_or_404(PullRequest, pk=pr_id, status=PullRequest.OPEN_STATUS)
        pr.close()
        return Response({}, status=status.HTTP_200_OK)
