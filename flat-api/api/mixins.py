
from rest_framework.views import APIView as rest_APIView


class APIView(rest_APIView):

    authentication_classes = []
    permission_classes = []
