from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ticket import views

urlpatterns = [
    path('', views.ListTickets.as_view()),
    path('flight/<int:pk>/', views.CreateFlightTicket.as_view()),
    path('<int:pk>/', views.TicketDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
