from rest_framework.serializers import ModelSerializer
from .models import Client, Contract, Event


# TODO: Serializer User


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id',
                  'first_name',
                  'last_name',
                  'company_name',
                  'sales_contact'
                  ]


class ClientDetailSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ContractListSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id',
                  'client',
                  'sales_contact',
                  'status',
                  ]


class ContractDetailSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id',
                  'client',
                  'support_contact',
                  'event_status',
                  ]


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
