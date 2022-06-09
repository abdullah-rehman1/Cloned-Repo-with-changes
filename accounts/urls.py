from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('accounts-all', views.AccountList.as_view()),
    # path('accounts-all/<int:pk>', views.AccountDetail.as_view()),
    # path('accounts-all/sign-in', views.signIn.as_view()),
    path('accounts/', include('djoser.urls')),
    path('accounts/', include('djoser.urls.authtoken')),
    path('accounts/get-token-with-userID/login', views.TokenObtainView.as_view(), name='new-token,obtain-view')
]