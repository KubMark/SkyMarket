from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):# Право доступа пользователя
    message = "You don't have the permission to make changes"

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        role = request.user.role

        return request.user.id == obj.author.id or role == "admin"
