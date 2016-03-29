from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from serializers import UserSerializer, OrdersSerializer, TruckSerializer, TripSerializer, DriverSerializer
from models import Orders, User, Truck, Trip, Driver



'''class OrdersList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Orders.objects.all()#.order_by('-date_joined')
    serializer_class = OrdersSerializer

class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer'''

class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


