from authtoken.models import InventoryUser
from rest_framework.serializers import ModelSerializer

class InventoryUserSerializer(ModelSerializer):
    class Meta:
        model = InventoryUser
        fields = ('__all__')