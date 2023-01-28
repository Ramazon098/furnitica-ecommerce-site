from rest_framework.permissions import BasePermission


# Create your permissions here.

class NotIsAuthenticated(BasePermission):
    message = 'You do not have permission to get the user list.'

    def has_permission(self, request, view):
        return bool(
            request.user and not request.user.is_authenticated,
        )


class NotIsAuthenticatedAndIsAdminSuper(BasePermission):
    message = 'You do not have permission to get the user list.'

    def has_permission(self, request, view):
        return bool(
            request.user and not request.user.is_authenticated or request.user.is_superuser,
        )
