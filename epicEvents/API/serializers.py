from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
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
