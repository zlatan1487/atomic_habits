from rest_framework import generics
from habits.paginators import Pagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from habits.permissions import IsOwnerOrReadOnly
from django.db.models import Q
from habits.tasks import remind_habits
from habits.models import (
    Place,
    Action,
    PleasantHabit,
    LinkedHabit,
    Habit
)
from habits.serializers import (
    PlaceSerializer,
    ActionSerializer,
    PleasantHabitSerializer,
    LinkedHabitSerializer,
    HabitSerializer
)


class HabitListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания объектов модели Habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # remind_habits()


class HabitListView(ListAPIView):
    """
    Представление для просмотра объектов модели Habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(Q(user=user)).order_by('id')
        return queryset


class HabitUpdateView(generics.UpdateAPIView):
    """
    Представление для редактирования объектов модели Habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class HabitDeleteView(generics.DestroyAPIView):
    """
    Представление для удаления объектов модели Habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class PublicHabitListView(generics.ListAPIView):
    """
    Представление для показа списка объектов модели Habit с публичным статусом.
    """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class PlaceListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания объектов модели Place.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]


class ActionListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания и списка объектов модели Action.
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]


class PleasantHabitListCreateView(generics.ListCreateAPIView):

    """
    Представление для создания и списка объектов модели PleasantHabit.
    """
    queryset = PleasantHabit.objects.all()
    serializer_class = PleasantHabitSerializer
    permission_classes = [IsAuthenticated]


class LinkedHabitListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания и списка объектов модели LinkedHabit.
    """
    queryset = LinkedHabit.objects.all()
    serializer_class = LinkedHabitSerializer
    permission_classes = [IsAuthenticated]