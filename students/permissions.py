from rest_framework import permissions

class studentPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return obj.course.id == request.student.course_id
        return True