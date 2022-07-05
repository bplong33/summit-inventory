from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions
from authtoken.authenticate import token_authentication
from .serializers import InventorySerializer
from .models import Inventory

# Create your views here.
@api_view(['GET'])
def get_product(request):
    payload = token_authentication(request)
    # if payload['permissions'] != 'read' or payload['permissions'] != '':
    if 'read' not in payload['permissions'] and 'admin' not in payload['permissions']:
        return Response(
            {'detail':"You do not have permissions for these actions",
             'Permissions':payload['permissions']}, 
            status='403')
        
    try:
        if 'name' in request.data:
            item_name = request.data['name']
            item = Inventory.objects.get(name=item_name)
        elif 'id' in request.data:
            item_id = request.data['id']
            item = Inventory.objects.get(id=item_id)
        else:
            raise Http404("Missing required data")

        serialize = InventorySerializer(item)
        return Response(serialize.data)
    except ObjectDoesNotExist:
        return Response({'detail':'Item not found'})

@api_view(['GET'])
def list_all_products(request):
    payload = token_authentication(request)
    if 'read' not in payload['permissions'] and 'admin' not in payload['permissions']:
        return Response(
            {'detail':"You do not have permissions for these actions",
             'Permissions':payload['permissions']}, 
            status='403')
    
    items = Inventory.objects.all()
    
    serialize = InventorySerializer(items, many=True)
    return Response(serialize.data)

@api_view(['POST'])
def add_product(request):
    payload = token_authentication(request)
    # if payload['permissions'] != '2' or payload['permissions'] != '3':
    if 'manage' not in payload['permissions'] and 'admin' not in payload['permissions']:
        return Response(
            {'detail':"You do not have permissions for these actions"}, 
            status='403')
    
    try:
        serializers = InventorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        else:
            raise KeyError
    except KeyError:
        raise Http404("Missing required data")
     
    return Response(status='200')
    
    

@api_view(['POST'])
def update_product(request, id):
    # payload = token_authentication(request)
    # if 'manage' not in payload['permissions'] and 'admin' not in payload['permissions']:
    #     return Response(
    #         {'detail':"You do not have permissions for these actions"}, 
    #         status='403')
    
    try:
        item = Inventory.objects.get(id=id)
        if 'name' in request.GET:
            item.name = request.GET.get('name')
        if 'description' in request.GET:
            item.description = request.GET.get('description')
        if 'quantity' in request.GET:
            item.quantity = request.GET.get('quantity')
        
        item.save()
        # serializer = InventorySerializer(item)
        return Response(status="200")
        # return Response(id)
        
    except ObjectDoesNotExist:
        return Response({'detail':'Item not found'})
    # return Response(request.GET)

@api_view(['POST'])
def soft_delete_product(request):
    payload = token_authentication(request)
    if payload['permissions'] != '2' or payload['permissions'] != '3':
        return Response(
            {'detail':"You do not have permissions for these actions"}, 
            status='403')

def hard_delete_product(request):
    pass