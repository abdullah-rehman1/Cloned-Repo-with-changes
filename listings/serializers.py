from rest_framework import fields, serializers
from .models import *

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'