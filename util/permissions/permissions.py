from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class CustomAdminUserPostDelete(permissions.BasePermission):
    """
    Won't allow post or delete for non admin user
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
            request.user.is_staff and
            request.user.is_authenticated):
            return True
        return False