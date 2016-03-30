from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from serializers import UserSerializer, OrdersSerializer, TruckSerializer, TripSerializer, DriverSerializer
from models import Orders, User, Truck, Trip, Driver
from django.http import HttpResponse
from rest_framework.response import Response



class OrdersList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()#.order_by('-date_joined')
    serializer_class = OrdersSerializer

class DriverList(APIView):#APIView):
    
    def get(self, request, format=None):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        queryset = Driver.objects.all()
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        request
        queryset = driver.objects.filter()


'''class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer'''

class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()#.order_by('-date_joined')
    serializer_class = TripSerializer

class TruckList(generics.ListCreateAPIView):
    queryset = Truck.objects.all()#.order_by('-date_joined')
    serializer_class = TruckSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()#.order_by('-date_joined')
    serializer_class = UserSerializer


