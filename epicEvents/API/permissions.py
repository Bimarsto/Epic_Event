from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return request.user.groups.filter(name='Admin').exists()
        return False


class SalesPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return request.user.groups.filter(name='Equipe de vente').exists()
        return False


class SupportPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return request.user.groups.filter(name='Equipe support').exists()
        return False
