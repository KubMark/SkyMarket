from rest_framework.permissions import BasePermission

from skymarket.users.managers import UserRoles


class IsOwner(BasePermission):# Право доступа пользователя
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAdmin(BasePermission):# Право доступа пользователя
    def has_permission(self, request, view):
        return request.user.role == UserRoles.ADMIN