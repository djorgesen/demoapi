from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework import viewsets

from rest_framework.response import Response
from djcore.models import User
from .serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from djcore.authentication import JSONWebTokenAuthentication

import json
# Create your views here.

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class ObtainJSONWebToken(APIView):
    """
API View that receives a POST with a user's username and password.

Returns a JSON Web Token that can be used for authenticated requests.
"""
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = JSONWebTokenSerializer



    def post(self, request):
        serializer = self.serializer_class(data=json.loads(request.body))
        if serializer.is_valid():
            return Response({'token': serializer.object['token']})
        return Response(serializer.errors)

    def get(self, request):
        return Response('invalid method', status=status.HTTP_400_BAD_REQUEST)

    def options(self,request):
        return Response('ok',status=status.HTTP_200_OK)