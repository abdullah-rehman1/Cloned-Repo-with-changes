from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('bookings-all', views.BookingList.as_view()),
    path('bookings-all/<int:pk>', views.BookingDetail.as_view()), 
    path('bookings-all/specific-listing-booking', views.SpecificListingBooking.as_view()),
    path('bookings-all/specific-tenant-booking', views.SpecificTenantBooking.as_view()),
    path('bookings-all/specific-realtor-booking', views.SpecificRealtorBooking.as_view()),
    path('bookings-all/specific-realtor-approved-booking', views.SpecificRealtorApprovedBooking.as_view()),
]
