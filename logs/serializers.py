from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ('log_id', 'log_open', 'log_date')