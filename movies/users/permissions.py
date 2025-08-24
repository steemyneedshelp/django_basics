from rest_framework import permissions

class IsStaff (permissions.BasePermission):
  def has_permssion(self, request, view):
    return bool(request.user and request.user.is_authenticated and request.user.role == 'staff_1')