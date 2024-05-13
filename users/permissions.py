from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверяет является ли пользователь модератором."""

    def has_permission(self, request, view) -> bool:
        return request.user.groups.filter(name="moderator").exists()


class IsOwner(permissions.BasePermission):
    """Проверяет является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj) -> bool:
        if obj.owner == request.user:
            return True
        return False


class IsStaff(permissions.BasePermission):
    """Проверяет является ли пользователь staff."""

    def has_permission(self, request, view) -> bool:
        if request.user.is_staff:
            return True
        return False
