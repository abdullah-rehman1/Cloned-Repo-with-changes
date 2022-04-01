from django.urls import re_path, include 
from django.contrib import admin
from django.urls import path, include, re_path
 
urlpatterns = [ 
    path('admin/', admin.site.urls),
    re_path(r'^', include('listings.urls')),
    re_path(r'^', include('listingsFeedback.urls')),
    re_path(r'^', include('booking.urls')),
]