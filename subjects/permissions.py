from rest_framework import permissions

class subjectPermission(permissions.BasePermission):

    def has_permission(self, request):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser