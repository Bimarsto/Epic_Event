from rest_framework.viewsets import ModelViewSet

from .models import Client, Contract, Event
from .serializers import ClientListSerializer, ClientDetailSerializer, \
                         ContractListSerializer, ContractDetailSerializer, \
                         EventListSerializer, EventDetailSerializer


class ClientViewSet(ModelViewSet):

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer

    def get_queryset(self):
        return Client.objects.all


class ContractViewSet(ModelViewSet):

    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer

    def get_queryset(self):
        return Contract.objects.all


class EventViewSet(ModelViewSet):

    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer

    def get_queryset(self):
        return Event.objects.all
