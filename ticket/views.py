"""Module containing the ticket views"""
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from ticket.serializers import TicketSerializer
from ticket.models import Ticket
from flight.models import Flight
from shared.authenticate_user import token_required


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
