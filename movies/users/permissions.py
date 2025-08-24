from rest_framework import permissions # type: ignore

class IsStaff (permissions.BasePermission):
  def has_permssion(self, request, view):
    return bool(request.user and request.user.is_authenticated and request.user.role == 'staff_1')