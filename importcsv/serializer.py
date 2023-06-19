from rest_framework import serializers
from .models import CSVSource


class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVSource
        fields = '__all__'
