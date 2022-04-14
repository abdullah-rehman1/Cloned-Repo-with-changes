from django.db import models
from django.shortcuts import get_object_or_404
from listings.models import Listing
from accounts.models import Account

# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    tenant_id = models.ForeignKey(Account, related_name='tenants', on_delete=models.CASCADE, null=True)
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    booking_date_time = models.DateTimeField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    def save(self, *args, **kwargs):
        tenant = get_object_or_404(Account, user_id=self.tenant_id.user_id)
        if tenant.user_type != 'Tenant':
            raise ValueError('TENANT_ID can not be REALTOR_ID')
        super().save(*args, **kwargs)
    