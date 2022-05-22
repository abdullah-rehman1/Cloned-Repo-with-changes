from django.views import View
from .serializers import AccountSerializer
from .models import Account as AccountModel
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class AccountList(generics.ListCreateAPIView):
    queryset = AccountModel.objects.all()
    serializer_class = AccountSerializer

class signIn(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    def get_queryset(self):
        queryset = AccountModel.objects.all()
        email = self.request.query_params.get('email')
        password = self.request.query_params.get('password')
        queryset = queryset.filter(email=email).filter(password=password)
        return queryset
class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountModel.objects.all()
    serializer_class = AccountSerializer

# class Account(View):
#     @api_view(['POST'])
#     def register(request):
#         serializer = AccountSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     @api_view(['POST'])
#     def signin(request):
#         queryset = AccountModel.objects.all()
#         email_id = request.GET.get('email', False)
#         password = request.GET.get('password', False)
#         queryset = queryset.filter(email_id_id=email_id).filter(password=password)
#         serializer = AccountSerializer(queryset, many=True)
#         return Response(serializer.data) 

# class Tenant(View):
#     @api_view(['GET','POST'])
#     def getAllTenants(request):
#         queryset = AccountModel.objects.all()
#         user_type = request.GET.get('user_type', False)
#         queryset = queryset.filter(user_type=user_type)
#         serializer = AccountSerializer(queryset, many=True)
#         return Response(serializer.data) 

#     @api_view(['GET','PUT','DELETE'])
#     def getTenantDetails(request, pk):
#         try:
#             account = AccountModel.objects.get(pk=pk)
#         except Account.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         if request.method == 'GET':
#             serializer = AccountSerializer(account)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = AccountSerializer(account, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             account.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT) 

# class Realtor:
#     @api_view(['GET','POST'])
#     def getAllRealtors(request):
#         queryset = AccountModel.objects.all()
#         user_type = request.GET.get('user_type', False)
#         queryset = queryset.filter(user_type=user_type)
#         serializer = AccountSerializer(queryset, many=True)
#         return Response(serializer.data) 

#     @api_view(['GET','PUT','DELETE'])
#     def getRealtorDetails(request, pk):
#         try:
#             account = AccountModel.objects.get(pk=pk)
#         except Account.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         if request.method == 'GET':
#             serializer = AccountSerializer(account)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = AccountSerializer(account, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             account.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT) 
