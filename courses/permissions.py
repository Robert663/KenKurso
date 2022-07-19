from rest_framework import permissions

class CoursePermission(permissions.BasePermission):

    def has_permission(self, request,views):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser