from rest_framework.permissions import BasePermission

class OwnerOrReadOnlyPerm(BasePermission):
    """Разрешает доступ всем пользователям"""

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user

class OwnerOnlyPerm(BasePermission):
    """Разрешает доступ только владельцу"""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
