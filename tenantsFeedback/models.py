from django.db import models
from django.shortcuts import get_object_or_404
from listings.models import Listing
from accounts.models import Account

# Create your models here.
class TenantFeedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    tenant_id = models.ForeignKey(Account, related_name='tenant_ids', on_delete=models.CASCADE, null=True)
    star_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    realtor_id = models.ForeignKey(Account, related_name='realtor_ids', on_delete=models.CASCADE, null=True)
    star_rating = models.CharField(max_length=100, choices=star_choices, default='1')
    description = models.TextField(blank=False)

    def save(self, *args, **kwargs):
        realtor = get_object_or_404(Account, user_id=self.realtor_id.user_id)
        if realtor.user_type != 'Realtor':
            raise ValueError('Realtor_ID can not be TENANT_ID')
        tenant = get_object_or_404(Account, user_id=self.tenant_id.user_id)
        if tenant.user_type != 'Tenant':
            raise ValueError('TENANT_ID can not be REALTOR_ID')
        super().save(*args, **kwargs)