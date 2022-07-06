import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .models import InventoryUser
from .serializers import InventoryUserSerializer
from .authenticate import user_authenticate, get_token
import jwt

# list_users and add_user endpoinds are for testing purposes
@api_view(['GET'])
def list_users(request):
    userlist = InventoryUser.objects.all()
    serializer = InventoryUserSerializer(userlist, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_user(request):
    serializer = InventoryUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def read_token(request):
    user = user_authenticate(request, 1)
    token = get_token(user, 'read')
    user.token = token
    user.save()
    return Response({"Token":token}, status="200")

@api_view(['POST'])
def manage_token(request):
    user = user_authenticate(request, 2)
    token = get_token(user, 'manage')
    user.token = token
    user.save()
    return Response({"Token":token}, status="200")

@api_view(['POST'])
def read_manage_token(request):
    user = user_authenticate(request, 3)
    token = get_token(user, 'read/manage')
    user.token = token
    user.save()
    return Response({"Token":token}, status="200")

@api_view(['POST'])
def admin_token(request):
    user = user_authenticate(request, 4)
    token = get_token(user, 'admin')
    user.token = token
    user.save()
    return Response({"Token":token}, status="200")