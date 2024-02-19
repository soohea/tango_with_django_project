from django.test import TestCase
from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there partner!")

