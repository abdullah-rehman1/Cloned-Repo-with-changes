from django.db import models
from listings.models import Listing

# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    booking_date_time = models.DateTimeField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()