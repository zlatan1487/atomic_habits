from rest_framework import permissions
from rest_framework.permissions import BasePermission
from habits.models import Habit


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "Вы не имеете права на удаление или редактирование публичных привычек других пользователей"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:

            return True

        return obj.user == request.user

