from django.shortcuts import render
from rest_framework import generics,fields, serializers
from .serializers import *
from .models import Listing

# Create your views here.
class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class SpecificRealtorListing(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    def get_queryset(self):
        queryset = Listing.objects.all()
        realtor_id = self.request.query_params.get('realtor_id')
        if realtor_id is not None:
            queryset = queryset.filter(realtor_id_id=realtor_id)
        return queryset

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer