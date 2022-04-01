from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('bookings-all', views.BookingList.as_view()),
    path('bookings-all/<int:pk>', views.BookingDetail.as_view()),
]
