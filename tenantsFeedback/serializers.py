from rest_framework import fields, serializers
from .models import *

class TenantFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantFeedback
        fields = '__all__'