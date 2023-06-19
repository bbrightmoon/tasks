from django.urls import path, include
from user.views import (
    ProfileView,
    EditProfile,
    SignIn,
    SignUp)
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView


urlpatterns = [
    path('register/', SignUp.as_view()),
    path('login/', SignIn.as_view()),
    path('profile/', ProfileView.as_view()),
    path('edit_prof/<int:id>/', EditProfile.as_view()),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='verify'),


]
