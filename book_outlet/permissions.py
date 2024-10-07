from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission


def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff