from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from distances.serializers import DistanceSerializer
# from gcm.api import DevicesViewSet
from rest_framework.permissions import AllowAny

from distances.models import Distance

# Create your views here.

def index(request):
    latest_distance_list = Distance.objects.order_by('-dist_date')[:20]
    context = {'latest_distance_list': latest_distance_list}
    return render(request, 'distances/index.html', context)

def detail(request, a_distance_id):
	distance = get_object_or_404(Distance, pk=a_distance_id)
	return render(request, 'distances/detail.html', {'distance': distance})

class DistanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows logs to be viewed or edited.
    """
    queryset = Distance.objects.order_by('-dist_date')[:20]
    serializer_class = DistanceSerializer