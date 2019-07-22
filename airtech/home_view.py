"""Module contains the views for airtech homepage"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def airtech_home(request):
    """Handle requests to the homepage"""
    data = {'message': 'Welcome to AirTech API' }
    return JsonResponse(data, safe=False)
