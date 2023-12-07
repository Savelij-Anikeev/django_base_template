from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or
                    (obj.username == request.user.username and
                     obj.email == request.user.email))
