from django.shortcuts import render
from rest_framework import generics,fields, serializers
from .serializers import *
from .models import Booking

# Create your views here.
class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer