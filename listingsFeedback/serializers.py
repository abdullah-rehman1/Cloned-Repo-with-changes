from rest_framework import fields, serializers
from .models import *

class ListingFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingFeedback
        fields = '__all__'