from django.urls import path
from .view import CSVView, CSVSourceView

urlpatterns = [
    path('', CSVView.as_view(), name='csvview'),
    path('unload/', CSVSourceView.as_view(), name='unload-csv'),
]
