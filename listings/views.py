from django.shortcuts import render
from rest_framework import generics,fields, serializers
from .serializers import *
from .models import Listing

# Create your views here.
class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer