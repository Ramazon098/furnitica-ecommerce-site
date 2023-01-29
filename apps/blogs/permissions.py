from rest_framework.permissions import BasePermission


# Create your permissions here.

class NotOrIsAuthenticated(BasePermission):
    message = 'You do not have permission to get the user list.'

    def has_permission(self, request, view):
        if request.method == 'GET':
            return bool(
                request.user and not request.user.is_authenticated,
            )
        else:
            return bool(
                request.user and request.user.is_authenticated,
            )
