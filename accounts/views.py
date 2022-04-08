from django.shortcuts import render
from rest_framework import generics,fields, serializers
from .serializers import *
from .models import Account

# Create your views here.
class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer