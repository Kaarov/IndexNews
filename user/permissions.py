from rest_framework.permissions import BasePermission

from user.models import *


class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == MANAGER:
            return True
        else:
            return False


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == USER:
            return True
        else:
            return False
