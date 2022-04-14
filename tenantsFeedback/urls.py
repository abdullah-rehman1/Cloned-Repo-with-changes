from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('tenantsfeedbacks-all', views.TenantFeedbackList.as_view()),
    path('tenantsfeedbacks-all/<int:pk>', views.TenantFeedbackDetail.as_view()),
    path('tenantsfeedbacks-all/specific-feedbacks/', views.SpecificListingFeedback.as_view()),
]
