from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from flight import views

urlpatterns = [
    path('', views.CreateListFlight.as_view()),
    path('<int:pk>/', views.FlightDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
