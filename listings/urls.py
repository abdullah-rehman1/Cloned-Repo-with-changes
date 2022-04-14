from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('listings-all', views.ListingList.as_view()),
    path('listings-all/<int:pk>', views.ListingDetail.as_view()),
    path('listings-all/specific-listings/', views.SpecificRealtorListing.as_view()),
]
