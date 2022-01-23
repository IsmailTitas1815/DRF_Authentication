from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from User_Login.views import *


router = DefaultRouter()
router.register(r'user', UserProfileViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('user/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
] + router.urls
