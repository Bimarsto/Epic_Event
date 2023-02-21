from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from API.views import ClientViewSet, ContractViewSet, EventViewSet

client_router = routers.SimpleRouter()
client_router.register('clients', ClientViewSet, basename='clients')

contract_router = routers.SimpleRouter()
contract_router.register('contracts', ContractViewSet, basename='contracts')

event_router = routers.SimpleRouter()
event_router.register('events', EventViewSet, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(client_router.urls)),
    path('api/', include(contract_router.urls)),
    path('api/', include(event_router.urls)),
]
