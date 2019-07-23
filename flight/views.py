"""Module containing the view for flight entity"""
from rest_framework import generics

from .models import Flight
from .serializers import FlightSerializer,FlightDetailSerializer


class CreateListFlight(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightDetailSerializer
    exclude = '__all__'
