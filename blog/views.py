from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Test
from .serializers import TestSerializer

# Create your views here.
def index(request):
    return HttpResponse("Triggering first Travis build.")

class TestView(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer