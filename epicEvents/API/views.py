from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from .permissions import AdminPermission, SalesPermission, SupportPermission, IsSuperUser
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer, UserSerializer


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission]
        else:
            permission_classes = [IsSuperUser | AdminPermission]
        return [permission() for permission in permission_classes]


class ContractViewSet(ModelViewSet):

    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission]
        else:
            permission_classes = [IsSuperUser | AdminPermission]
        return [permission() for permission in permission_classes]


class EventViewSet(ModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsSuperUser | AdminPermission | SupportPermission]
        else:
            permission_classes = [IsSuperUser | AdminPermission]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update']:
            permission_classes = [IsSuperUser | AdminPermission]
        else:
            permission_classes = [IsSuperUser]
        return [permission() for permission in permission_classes]
