from rest_framework.permissions import BasePermission

class Owner(BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.added_by == request.user
    