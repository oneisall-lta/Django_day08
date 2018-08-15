from django.urls import path

from errorapp import views

urlpatterns = [
    path('compute/',views.computer)
]