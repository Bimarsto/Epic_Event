from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Client, Contract, Event


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
