from django.shortcuts import render
from rest_framework import generics,fields, serializers
from tenantsFeedback.models import TenantFeedback
from tenantsFeedback.serializers import TenantFeedbackSerializer
from rest_framework import generics

# Create your views here.
class TenantFeedbackList(generics.ListCreateAPIView):
    queryset = TenantFeedback.objects.all()
    serializer_class = TenantFeedbackSerializer

class SpecificListingFeedback(generics.ListCreateAPIView):
    serializer_class = TenantFeedbackSerializer
    def get_queryset(self):
        queryset = TenantFeedback.objects.all()
        tenant_id = self.request.query_params.get('tenant_id')
        if tenant_id is not None:
            queryset = queryset.filter(tenant_id_id=tenant_id)
        return queryset

class TenantFeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TenantFeedback.objects.all()
    serializer_class = TenantFeedbackSerializer