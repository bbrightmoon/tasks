from django.urls import path
from chat import view


urlpatterns = [
    path('room/<int:pk>/', view.room, name='room'),
    path('', view.index, name='index'),
]
