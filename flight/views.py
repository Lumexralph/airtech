"""Module containing the view for flight entity"""
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms import model_to_dict

from account.models import User
from shared.authenticate_user import token_required
from .models import Flight
from .serializers import FlightSerializer, FlightDetailSerializer
from services.send_email import send_email_to


class CreateListFlight(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @token_required
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightDetailSerializer

    @token_required
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @token_required
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @token_required
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FlightReservation(generics.RetrieveUpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @token_required
    def put(self, request, *args, **kwargs):
        data = self.update(request, *args, **kwargs)

        if data:
            return Response(data.data, status=status.HTTP_200_OK)

        return Response({
            'error': 'Flight or user does not exists in our system'
        }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        flight_id = kwargs.get('pk')
        flight = Flight.objects.filter(pk=flight_id).first()
        user_email = request.user['data']['user_info']['email']
        user = User.objects.filter(email=user_email).first()

        if flight and user:
            # check if the flight is still available
            if flight.available_seats > 0:
                flight.available_seats -= 1
                flight.reservations = user
                flight.save()
                flight_dict = model_to_dict(flight)
                serializer = self.get_serializer(data=flight_dict)
                serializer.is_valid(raise_exception=True)

                send_email_to(
                    'Airtech Flight Ticket',
                    user_email,
                    f'Flight Type: {flight.flight_type}' \
                    f'Departure Date: {flight.departure_date}' \
                    f'Location: {flight.to_location}'
                )

                return serializer



    @token_required
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
