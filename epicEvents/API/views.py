from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from .permissions import AdminPermission, SalesPermission, SupportPermission, IsSuperUser
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer, UserSerializer


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer

    def get_queryset(self):
        user_group = str(self.request.user.groups.get())
        if 'Admin' == user_group:
            return Client.objects.all()
        elif 'Equipe de vente' == user_group:
            return Client.objects.filter(sales_contact=self.request.user)
        elif 'Equipe support' == user_group:
            client_events = Event.objects.filter(support_contact=self.request.user)
            list_clients = []
            for event in client_events:
                if event.client not in list_clients:
                    list_clients.append(event.client)
            return list_clients

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
        user_group = str(self.request.user.groups.get())
        if 'Admin' == user_group:
            return Contract.objects.all()
        else:
            return Contract.objects.filter(sales_contact=self.request.user)

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
        user_group = str(self.request.user.groups.get())
        if 'Admin' == user_group:
            return Event.objects.all()
        else:
            return Event.objects.filter(support_contact=self.request.user)

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
