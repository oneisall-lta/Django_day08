from django.urls import path

from homework import views
app_name = 'homework'

urlpatterns = [
    path('addstu/', views.addstu, name='addstu'),
    path('addgrade/', views.addgrade, name='addgrade'),
    path('gograde/', views.go_grade),
    path('gostu/', views.go_stu, name='gostu'),
    path('showstu/',views.show_student)

]
