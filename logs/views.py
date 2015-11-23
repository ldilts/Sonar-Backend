from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from logs.serializers import LogSerializer

from logs.models import Log

# Create your views here.

def index(request):
    latest_log_list = Log.objects.order_by('-log_date')[:50]
    context = {'latest_log_list': latest_log_list}
    return render(request, 'logs/index.html', context)

def detail(request, a_log_id):
	log = get_object_or_404(Log, pk=a_log_id)
	return render(request, 'logs/detail.html', {'log': log})

class LogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows logs to be viewed or edited.
    """
    queryset = Log.objects.order_by('-log_date')[:50]
    serializer_class = LogSerializer