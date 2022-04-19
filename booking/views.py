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

class SpecificListingBooking(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        queryset = Booking.objects.all()
        list_id = self.request.query_params.get('list_id')
        if list_id is not None:
            queryset = queryset.filter(list_id_id=list_id)
        return queryset        

class SpecificTenantBooking(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        queryset = Booking.objects.all()
        tenant_id = self.request.query_params.get('tenant_id')
        if tenant_id is not None:
            queryset = queryset.filter(tenant_id_id=tenant_id)    
        return queryset

class SpecificRealtorBooking(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        queryset = Booking.objects.all()
        realtor_id = self.request.query_params.get('realtor_id')
        if realtor_id is not None:
            queryset = queryset.filter(realtor_id_id=realtor_id)    
        return queryset  