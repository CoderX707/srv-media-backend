from django.shortcuts import render
from channels_api.serializer import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from channels_api.models import Category, Subcription
from rest_framework.exceptions import AuthenticationFailed
import jwt
from channels_api.serializer import SubscriptionSerializer

# Create your views here.


def authChecker(request):
    if not 'token' in request.data:
        raise AuthenticationFailed('Token missing!')
    token = request.data['token']
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    except (jwt.InvalidTokenError, jwt.ExpiredSignatureError, jwt.DecodeError):
        raise AuthenticationFailed('Unauthenticated!')


class ChannelsView(APIView):
    def post(self, request):
        authChecker(request)
        Channels = Category.objects.all()
        serializer = CategorySerializer(Channels, many=True)
        return Response(serializer.data)


class SubscriptionDetails(APIView):
    def post(self, request):
        authChecker(request)
        serializer = SubscriptionSerializer(
            data=request.data['subscriptionDetails'], many=True)
        test = serializer.is_valid(raise_exception=True)
        if test == True:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class SubscriptionByUser(APIView):
    def post(self, request):
        authChecker(request)
        if not 'user_id' in request.data:
            return Response({"error": "user id missing"})
        subcriptions = Subcription.objects.filter(user_id=request.data['user_id'])
        serializer = SubscriptionSerializer(subcriptions, many=True)
        return Response(serializer.data)
