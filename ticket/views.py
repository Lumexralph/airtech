"""Module containing the ticket views"""
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from django.forms import model_to_dict

from ticket.serializers import TicketSerializer
from ticket.models import Ticket
from flight.models import Flight
from account.models import User
from shared.authenticate_user import token_required
from services.send_email import send_email_to


class CreateFlightTicket(mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @token_required
    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        if data:
            headers = self.get_success_headers(data.data)
            return Response(data.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response({
            'error': 'the flight for the ticket could not be found'
        }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        flight_id = kwargs.get('pk')
        flight = Flight.objects.filter(pk=flight_id).first()

        if flight:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            ticket = serializer.save()
            flight.ticket = ticket
            flight.save()
            return serializer


class ListTickets(mixins.ListModelMixin,
                  generics.GenericAPIView):
    """Class for listing all tickets"""
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


    @token_required
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    """Serializer for a ticket"""
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @token_required
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @token_required
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @token_required
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BookTicket(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @token_required
    def put(self, request, *args, **kwargs):
        data = self.update(request, *args, **kwargs)

        if data:
            return Response(data, status=status.HTTP_200_OK)

        return Response({
            'error': 'Flight or user does not exists in our system'
        }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        ticket_id = kwargs.get('pk')
        ticket = Ticket.objects.filter(pk=ticket_id).first()
        user_email = request.user['data']['user_info']['email']
        user = User.objects.filter(email=user_email).first()

        if ticket and user:
            flight = ticket.flight.all().first()
            if flight.available_seats > 0:
                flight.available_seats -= 1
                ticket.owners = user
                ticket.booked = True
                ticket.save()
                flight.save()
                ticket = model_to_dict(ticket)

                send_email_to(
                    'Airtech Flight Ticket',
                    user_email,
                    f'Flight Type: {flight.flight_type}' \
                    f'Departure Date: {flight.departure_date}' \
                    f'Location: {flight.to_location}'
                )

                return {
                    'ticket': ticket,
                    'owner': model_to_dict(user),
                    'flight_details': model_to_dict(flight),
                }
