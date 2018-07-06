from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Language, Programmer, Paradigm
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer


class LanguageView(viewsets.ModelViewSet):
   queryset = Language.objects.all()
   serializer_class = LanguageSerializer


class ProgrammerView(viewsets.ModelViewSet):
 queryset = Programmer.objects.all()
 serializer_class = ProgrammerSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer



