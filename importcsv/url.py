from django.urls import path
from .view import CSVView

urlpatterns = [
    path('', CSVView.as_view(), name='csvview')
]
