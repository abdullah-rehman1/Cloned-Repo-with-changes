from .serializers import *
from .models import Listing as ListingModel
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View
from rest_framework import generics

class ListingList(generics.ListCreateAPIView):
    queryset = ListingModel.objects.all()
    serializer_class = ListingSerializer

class SpecificRealtorListing(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    def get_queryset(self):
        queryset = ListingModel.objects.all()
        realtor_id = self.request.query_params.get('realtor_id')
        is_featured = self.request.query_params.get('is_featured')
        if realtor_id is not None:
            queryset = queryset.filter(realtor_id_id=realtor_id)
        elif is_featured is not None:
            queryset = queryset.filter(is_featured=is_featured)
        return queryset

class SpecificRealtorFeaturedListing(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    def get_queryset(self):
        queryset = ListingModel.objects.all()
        realtor_id = self.request.query_params.get('realtor_id')
        is_featured = self.request.query_params.get('is_featured')
        queryset = queryset.filter(realtor_id_id=realtor_id).filter(is_featured=is_featured)
        return queryset
        
class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingModel.objects.all()
    serializer_class = ListingSerializer
