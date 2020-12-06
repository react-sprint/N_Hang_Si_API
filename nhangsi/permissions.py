from django.conf import settings

from rest_framework.permissions import BasePermission


class Check_API_KEY(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('N-Hang-Si-Api') == settings.N_HANG_SI_API_KEY
