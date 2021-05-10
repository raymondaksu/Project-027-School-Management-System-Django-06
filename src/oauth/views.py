import requests
from decouple import config

from rest_framework import serializers, generics, status, permissions
from rest_framework.response import Response


class GithubCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255, required=True)
    clientId = serializers.CharField(max_length=255)
    redirectUri = serializers.CharField(max_length=255)

class GithubCodeView(generics.GenericAPIView):
    serializer_class = GithubCodeSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        ACCESS_URL = 'https://github.com/login/oauth/access_token'

        payload = {
            'code' : request.data['code'],
            'client_id' : config('GITHUB_CLIENT_ID'),
            'client_secret' : config('GITHUB_CLIENT_SECRET'),
        }
        headers = {
            'Accept' : 'application/json'
        }
        res = requests.post(ACCESS_URL, payload, headers=headers)

        return Response(res.text, status=status.HTTP_200_OK)