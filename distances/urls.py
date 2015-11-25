from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /logs/
    url(r'^$', views.index, name='index'),
    # ex: /logs/5/
    url(r'^(?P<a_distance_id>[0-9]+)/$', views.detail, name='detail'),
]