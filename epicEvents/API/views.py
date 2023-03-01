from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .permissions import AdminPermission, SalesPermission, SupportPermission
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer


class ClientViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [AdminPermission | SalesPermission]
        else:
            permission_classes = [AdminPermission]
        return [permission() for permission in permission_classes]


class ContractViewSet(ModelViewSet):

    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [AdminPermission | SalesPermission]
        else:
            permission_classes = [AdminPermission]
        return [permission() for permission in permission_classes]


class EventViewSet(ModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create']:
            permission_classes = [AdminPermission | SalesPermission]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [AdminPermission | SupportPermission]
        else:
            permission_classes = [AdminPermission]
        return [permission() for permission in permission_classes]
