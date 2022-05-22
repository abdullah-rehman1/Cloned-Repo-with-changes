from django.urls import include, path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('bookings-all', BookingList.as_view()),
    path('bookings-all/<int:pk>', BookingDetail.as_view()), 
    path('bookings-all/specific-listing-booking', SpecificListingBooking.as_view()),
    path('bookings-all/specific-tenant-booking', SpecificTenantBooking.as_view()),
    path('bookings-all/specific-realtor-booking', SpecificRealtorApprovedBooking.as_view()),
    path('bookings-all/specific-realtor-approved-booking', SpecificRealtorApprovedBooking.as_view()),
]
