from django.urls import path
from emailapp.views import *

urlpatterns = [
    path('goemail/',goemail),
    path('getemail/<int:state_code>', get_emails),
]