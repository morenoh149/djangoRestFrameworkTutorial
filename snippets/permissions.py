from rest_framework import permissions


class IsOwnerReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allow to any request,
        # so we'll always allow Get, head or options requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the ownder of the snippet.
        return obj.owner == request.user
