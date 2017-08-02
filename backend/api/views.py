# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice
from django import forms
# Create your views here.


class QuestionCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new question."""
        serializer.save()

class QuestionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ handle GET, PUT, DELETE requests """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new question."""
        serializer.save()

class ChoiceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ handle GET, PUT, DELETE requests """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    