from rest_framework import permissions

class SubjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.is_superuser)
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser