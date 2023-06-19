from django.urls import path
from social_auth.view import GoogleSocialAuthView

urlpatterns = [
    path('', GoogleSocialAuthView.as_view()),
]
