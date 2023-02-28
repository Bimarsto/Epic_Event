from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Client, Contract, Event


# class UserSignupSerializer(ModelSerializer):
#
#     tokens = SerializerMethodField()
#
#     class Meta:
#         model = AUTH_USER_MODEL
#         fields = ['id',
#                   'first_name',
#                   'last_name',
#                   'email',
#                   'password',
#                   'tokens']
#
#     @staticmethod
#     def validate_password(value):
#         if value is not None:
#             return make_password(value)
#         raise ValidationError("Password is empty")
#
#     @staticmethod
#     def get_tokens(instance):
#         tokens = RefreshToken.for_user(instance)
#         data = {
#             'refresh': str(tokens),
#             'access': str(tokens.access_token)
#         }
#         return data


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
