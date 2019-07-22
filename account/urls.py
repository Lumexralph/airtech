from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    path('signup', views.UserRegistration.as_view()),
    path('login', views.UserLogin.as_view()),
    path('accounts/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
