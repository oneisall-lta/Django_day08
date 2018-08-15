from django.urls import path
from cacheapp.views import *

urlpatterns = [
    path('cake/<cake_id>/', memcached_getdata),
]
