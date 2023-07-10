from rest_framework import serializers
from importcsv.models import CSVSource


class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVSource
        fields = '__all__'
