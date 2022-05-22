from rest_framework import generics
from .models import TenantFeedback as TenantFeedbackModel
from .serializers import TenantFeedbackSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View

class TenantFeedback(View):
    @api_view(['GET','POST'])
    def getAllTenantFeedbacks(request):
        if request.method == 'GET':
            listings = TenantFeedbackModel.objects.all()
            serializer = TenantFeedbackSerializer(listings, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = TenantFeedbackSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @api_view(['POST'])
    def postTenantFeedback(request):
        serializer = TenantFeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @api_view(['GET'])
    def getTenantFeedbackDetails(request, pk):
        try:
            tenantFeedback = TenantFeedbackModel.objects.get(pk=pk)
        except TenantFeedback.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = TenantFeedbackSerializer(tenantFeedback)
            return Response(serializer.data)

    @api_view(['GET'])
    def getTenantFeedbackByRealtor(request):
        queryset = TenantFeedbackModel.objects.all()
        realtor_id = request.GET.get('realtor_id', False)
        if realtor_id!=False:
            queryset = queryset.filter(realtor_id_id=realtor_id)
        serializer = TenantFeedbackSerializer(queryset, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def getTenantFeedbackByTenant(request):
        queryset = TenantFeedbackModel.objects.all()
        tenant_id = request.GET.get('tenant_id', False)
        if tenant_id!=False:
            queryset = queryset.filter(tenant_id_id=tenant_id)
        serializer = TenantFeedbackSerializer(queryset, many=True)
        return Response(serializer.data)


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