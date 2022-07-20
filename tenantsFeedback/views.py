from rest_framework import generics
from .models import TenantFeedback as TenantFeedbackModel
from .serializers import TenantFeedbackSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View

# Create your views here.
class TenantFeedbackList(generics.ListCreateAPIView):
    queryset = TenantFeedbackModel.objects.all()
    serializer_class = TenantFeedbackSerializer

class SpecificTenantFeedback(generics.ListCreateAPIView):
    serializer_class = TenantFeedbackSerializer
    def get_queryset(self):
        queryset = TenantFeedbackModel.objects.all()
        tenant_id = self.request.query_params.get('tenant_id')
        realtor_id = self.request.query_params.get('realtor_id')
        if tenant_id is not None:
            queryset = queryset.filter(tenant_id_id=tenant_id)
        elif realtor_id is not None:
            queryset = queryset.filter(realtor_id_id=realtor_id)
        return queryset

class TenantFeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TenantFeedbackModel.objects.all()
    serializer_class = TenantFeedbackSerializer