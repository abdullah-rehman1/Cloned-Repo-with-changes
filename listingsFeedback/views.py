from rest_framework import generics
from .models import ListingFeedback
from .serializers import ListingFeedbackSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View

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