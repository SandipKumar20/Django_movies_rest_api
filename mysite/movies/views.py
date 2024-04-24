from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="action")
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="comedy")
    serializer_class = MovieSerializer


class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="thriller")
    serializer_class = MovieSerializer
