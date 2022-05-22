from django.urls import include, path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('listings-all', ListingList.as_view()),
    path('listings-all/<int:pk>', ListingDetail.as_view()),
    path('listings-all/specific-listings/', SpecificRealtorListing.as_view()),
    path('listings-all/specific-realtor-featured-listings/', SpecificRealtorFeaturedListing.as_view()),
]
