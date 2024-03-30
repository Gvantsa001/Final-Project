from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializer import EventSerializer
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.
@api_view(['GET'])
def getEvent(request):
   eventsapp = Event.objects.all()
   serializer = EventSerializer(eventsapp, many=True)
   return Response()


@api_view(['POST'])
def postEvent(request):
   return Response()



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventListCreateAPIView(generics.ListCreateAPIView):
   queryset = Event.objects.all()
   serializer_class = EventSerializer


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Event.objects.all()
   serializer_class = EventSerializer