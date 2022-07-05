from rest_framework.serializers import ModelSerializer
from inventory.models import Inventory

class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('__all__')