from django.urls import path
from .view import GoogleSocialAuthView

urlpatterns = [
    path('', GoogleSocialAuthView.as_view()),
]
