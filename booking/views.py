from django.views import View
from .serializers import BookingSerializer
from .models import Booking as BookingModel
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

class Booking(View):
    @api_view(['GET','POST'])
    def getAllBookings(request):
        if request.method == 'GET':
            bookings = BookingModel.objects.all()
            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = BookingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @api_view(['POST'])
    def postBooking(request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @api_view(['GET','PUT','DELETE'])
    def getBookingDetails(request, pk):
        try:
            booking = BookingModel.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BookingSerializer(booking, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            booking.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['GET'])
    def getBookingsByListing(request):
        queryset = BookingModel.objects.all()
        list_id = request.GET.get('list_id', False)
        if list_id!=False:
            queryset = queryset.filter(list_id_id=list_id)
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def getBookingsByTenant(request):
        queryset = BookingModel.objects.all()
        tenant_id = request.GET.get('tenant_id', False)
        if tenant_id!=False:
            queryset = queryset.filter(tenant_id_id=tenant_id)
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def getBookingsByRealtor(request):
        queryset = BookingModel.objects.all()
        realtor_id = request.GET.get('realtor_id', False)
        if realtor_id!=False:
            queryset = queryset.filter(realtor_id_id=realtor_id)
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)   

class Approved_Booking(View):
    @api_view(['GET'])
    def getApprovedBookingsByRealtor(request):
        queryset = BookingModel.objects.all()
        realtor_id = request.GET.get('realtor_id', False)
        is_approved = request.GET.get('is_approved', False)
        queryset = queryset.filter(realtor_id_id=realtor_id).filter(is_approved=is_approved)
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data) 

    @api_view(['PUT'])
    def approveBooking(request,pk):
        try:
            booking = BookingModel.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = BookingSerializer(booking, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Create your Generic views here.
    #
    #
class BookingList(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer

class SpecificListingBooking(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        queryset = BookingModel.objects.all()
        list_id = self.request.query_params.get('list_id')
        if list_id is not None:
            queryset = queryset.filter(list_id_id=list_id)
        return queryset        

class SpecificTenantBooking(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        queryset = BookingModel.objects.all()
        tenant_id = self.request.query_params.get('tenant_id')
        if tenant_id is not None:
            queryset = queryset.filter(tenant_id_id=tenant_id)    
        return queryset

class SpecificRealtorBooking(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        queryset = BookingModel.objects.all()
        realtor_id = self.request.query_params.get('realtor_id')
        if realtor_id is not None:
            queryset = queryset.filter(realtor_id_id=realtor_id)    
        return queryset  

class SpecificRealtorApprovedBooking(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        queryset = BookingModel.objects.all()
        realtor_id = self.request.query_params.get('realtor_id')
        is_approved = self.request.query_params.get('is_approved')
        queryset = queryset.filter(realtor_id_id=realtor_id).filter(is_approved=is_approved)
        return queryset