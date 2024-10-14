# from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission


# def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.author == request.user or request.user.is_staff
    

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrAdmin(BasePermission):
    """
    Custom permission to only allow authors of a book or admin to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff
    