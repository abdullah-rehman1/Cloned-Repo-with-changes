from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('listingfeedbacks-all', views.SpecificListingFeedback.as_view()),
    path('listingfeedbacks-all/<int:pk>', views.ListingFeedbackDetail.as_view()),
    #path('listings-all/listingfeedbacks-all/', views.SpecificListingFeedbacks.as_view()),
    #http://example.com/api/purchases
]
