from rest_framework import serializers
from .models import Items, OrderForm


#
# class ItemsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Items
#         fields = ('item_Position', 'item_Quantity')

# class ItemsSerializer(serializers.ModelSerializer):
#     order_form = OrderFormSerializer()
#
#     class Meta:
#         model = Items
#         fields = ('item_Position', 'item_Quantity', 'order_form')


class OrderFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderForm
        fields = ('clientId', 'orderId', 'state')


class ItemSerialier(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('client', 'id', 'position', 'quantity', 'state')


class OderSerialier(serializers.Serializer):
    clientId = serializers.CharField(max_length=200)
    orderId = serializers.CharField(max_length=200)
    items = ItemSerialier(many=True, default=None)
