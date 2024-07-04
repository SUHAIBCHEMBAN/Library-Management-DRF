from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to perform actions.
    """

    def has_permission(self, request, view):
        # Allow read-only access for non-authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Restrict write (POST, PUT, DELETE) for authenticated users only
        return request.user and request.user.is_authenticated
