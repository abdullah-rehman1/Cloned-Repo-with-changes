from django.db import models
from django.shortcuts import get_object_or_404
from accounts.models import Account

# Create your models here.
class Listing(models.Model):
    list_id = models.AutoField(primary_key=True)
    realtor_id = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    Nearby_University = models.CharField(max_length=100, default='Some Nearby University')
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    seater = models.IntegerField() 
    bathrooms = models.IntegerField()
    hostel_choices = (
        ('Boys Hostel', 'Boys Hostel'),
        ('Girls Hostel', 'Girls Hostel'),
    )
    hostel_type = models.CharField(max_length=100, choices=hostel_choices, default='Male')
    food_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    food_facility = models.CharField(max_length=100, choices=food_choices, default='Yes')
    laundary_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    laundary_facility = models.CharField(max_length=100, choices=laundary_choices, default='Yes')
    internet_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    internet_facility = models.CharField(max_length=100, choices=internet_choices, default='Yes')
    is_featured = models.BooleanField(default=False)
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photo1')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photo2')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        realtor = get_object_or_404(Account, user_id=self.realtor_id.user_id)
        if realtor.user_type != 'Realtor':
            raise ValueError('selected user must be realtor')
        super().save(*args, **kwargs)
    