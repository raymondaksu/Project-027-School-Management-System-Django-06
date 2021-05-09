from rest_framework import permissions


class ObjectPermission(permissions.BasePermission):
    """
    Check that user is object owner
    """

    def has_permission(self, request, view, obj):
        return obj.id == request.user