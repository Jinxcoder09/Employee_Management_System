from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Performance
from .serializers import PerformanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filterset_fields = ['review_date', 'rating', 'employee']
