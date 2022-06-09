from .serializers import *
from .models import Listing as ListingModel
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View
from rest_framework import generics

class Listing(View):

    @api_view(['GET','POST'])
    def getAllListings(request):
        if request.method == 'GET':
            listings = ListingModel.objects.all()
            serializer = ListingSerializer(listings, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ListingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @api_view(['POST'])
    def postListing(request):
        serializer = ListingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @api_view(['GET'])
    def getListingDetails(request, pk):
        try:
            listing = ListingModel.objects.get(pk=pk)
        except Listing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = ListingSerializer(listing)
            return Response(serializer.data)

    @api_view(['GET'])
    def getListingsByRealtor(request):
        queryset = ListingModel.objects.all()
        realtor_id = request.GET.get('realtor_id', False)
        if realtor_id!=False:
            queryset = queryset.filter(realtor_id_id=realtor_id)
        else:
            queryset = ListingModel.objects.all()
            is_featured = request.GET.get('is_featured', False)
            if is_featured!=False:
                queryset = queryset.filter(is_featured=is_featured)
        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def getAllFeaturedListings(request):
        queryset = ListingModel.objects.all()
        is_featured = request.GET.get('is_featured', False)
        if is_featured!=False:
            queryset = queryset.filter(is_featured=is_featured)
        return queryset

    @api_view(['GET'])
    def getFeaturedListingsByRealtor(request):
        queryset = ListingModel.objects.all()
        realtor_id = request.GET.get('realtor_id', False)
        is_featured = request.GET.get('is_featured', False)
        queryset = queryset.filter(realtor_id_id=realtor_id).filter(is_featured=is_featured)
        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)


#Create your views here.

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
