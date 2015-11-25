from rest_framework import serializers
from .models import Distance

class DistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distance
        fields = ('dist_id', 'dist_distance', 'dist_date')