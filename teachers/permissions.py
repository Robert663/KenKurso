from rest_framework import permissions

class teacherPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        
        return request.teacher.is_staff