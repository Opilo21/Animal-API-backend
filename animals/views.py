from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from rest_framework import generics 
from .models import Animal
from .serializers import AnimalSerializer



class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

