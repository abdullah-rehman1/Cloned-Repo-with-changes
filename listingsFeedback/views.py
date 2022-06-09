from rest_framework import generics
from .models import ListingFeedback
from .serializers import ListingFeedbackSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View

# class ListingFeedback(View):
#     @api_view(['GET','POST'])
#     def getAllListingFeedbacks(request):
#         if request.method == 'GET':
#             listings = ListingFeedbackModel.objects.all()
#             serializer = ListingFeedbackSerializer(listings, many=True)
#             return Response(serializer.data)
#         elif request.method == 'POST':
#             serializer = ListingFeedbackSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)

#     @api_view(['POST'])
#     def postListingFeedback(request):
#         serializer = ListingFeedbackSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     @api_view(['GET'])
#     def getListingFeedbackDetails(request, pk):
#         try:
#             listingFeedback = ListingFeedbackModel.objects.get(pk=pk)
#         except ListingFeedback.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         if request.method == 'GET':
#             serializer = ListingFeedbackSerializer(listingFeedback)
#             return Response(serializer.data)

#     @api_view(['GET'])
#     def getListingFeedbackByListing(request):
#         queryset = ListingFeedbackModel.objects.all()
#         realtor_id = request.GET.get('list_id', False)
#         if realtor_id!=False:
#             queryset = queryset.filter(realtor_id_id=realtor_id)
#         serializer = ListingFeedbackSerializer(queryset, many=True)
#         return Response(serializer.data)

# Create your views here.
class ListingFeedbackList(generics.ListCreateAPIView):
    queryset = ListingFeedback.objects.all()
    serializer_class = ListingFeedbackSerializer

class SpecificListingFeedback(generics.ListCreateAPIView):
    serializer_class = ListingFeedbackSerializer
    def get_queryset(self):
        queryset = ListingFeedback.objects.all()
        list_id = self.request.query_params.get('list_id')
        if list_id is not None:
            queryset = queryset.filter(list_id_id=list_id)
        return queryset

class ListingFeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingFeedback.objects.all()
    serializer_class = ListingFeedbackSerializer