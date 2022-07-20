from rest_framework import permissions

class StudentPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id