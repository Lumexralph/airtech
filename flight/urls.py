from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from flight import views

urlpatterns = [
    path('', views.CreateListFlight.as_view(), name='create-flight'),
    path('<int:pk>/', views.FlightDetail.as_view()),
    path('<int:pk>/reservations', views.FlightReservation.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
