from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrderForm, Items
from rest_framework import generics
from .serializers import ItemSerialier, OrderFormSerializer, OderSerialier
import json


# push_data=[]
# Create your views here.
class GetOrderAPIView(APIView):
    # globals push_data
    def post(self, request):
        # data = request.data

        my_data = OderSerialier(data=request.data)
        print(my_data)
        if not my_data.is_valid():
            return Response('sai du lieu', status=status.HTTP_400_BAD_REQUEST)
            my_data.save()
        # push_data=my_data.data['items']
        id_client = my_data.data['clientId']
        id_order = my_data.data['orderId']
        items = my_data.data['items']

        cf = OrderForm.objects.create(clientId=id_client, orderId=id_order, state=False)
        for i in items:
            ci = Items.objects.create(id=i['id'], position=i['position'], quantity=i['quantity'],
                                      order_Form=cf)
            ci.save()

        return Response(my_data.data, status=status.HTTP_200_OK)

    def get(self, request):

        # buffer = Items.objects.filter(status=False).order_by('-id')
        buffer = Items.objects.filter(order_Form__state=False)
        item_list = ItemSerialier(buffer, many=True)

        donhang = OrderForm.objects.filter(state=False).update(state=True)
        #donhang.save()
        # if item_list.is_valid():
        #     OrderForm.objects.filter(state=False).update(state=True)
        return Response(data=item_list.data, status=status.HTTP_200_OK)
        # OrderForm.objects.filter(state=True).update(state=False)
# class PushOrderAPIView(APIView):
