from django.db import models
from listings.models import Listing

# Create your models here.
class ListingFeedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    star_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    star_rating = models.CharField(max_length=100, choices=star_choices, default='1')
    description = models.TextField(blank=False)