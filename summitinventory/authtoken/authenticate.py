import datetime
from django.conf import settings
from django.http import Http404
from rest_framework import exceptions
from rest_framework.response import Response
from .models import InventoryUser
import jwt

def token_authentication(request):
    try:
        token = request.headers['Authorization'].split()
        if token[0] == "Bearer":
            payload = jwt.decode(token[1], settings.SECRET_KEY, 
                                 algorithms=['HS512'])   
            user = InventoryUser.objects.get(username=payload['username'])
    except jwt.DecodeError:
        raise exceptions.AuthenticationFailed("Invalid Token")
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed("Token has expired")
    except KeyError:
        raise Http404("Authorization token not provided")
    if user.token != token[1]:
        raise exceptions.AuthenticationFailed("A more recent session/token is in use")
    return (payload)

def user_authenticate(request, permissions):
    try:
        username = request.data['username']
        password = request.data['password']
    except:
        raise exceptions.AuthenticationFailed("Username/Password not provided")
    
    user = InventoryUser.objects.get(username=username)
    if user and user.password == password:
        if user.permissions != permissions:
            raise exceptions.AuthenticationFailed("User lacks to appropriate permissions")
        return user
    else:
        raise exceptions.AuthenticationFailed("User not found.")
    
def get_token(user, perms):
    data = {
            "username": user.username,
            "permissions": perms,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }
    token = jwt.encode(data,key=settings.SECRET_KEY, algorithm="HS512")
    return token
    
    