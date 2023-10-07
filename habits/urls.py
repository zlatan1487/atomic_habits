from django.urls import path
from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter

from habits.views import (
    PlaceListCreateView,
    ActionListCreateView,
    PleasantHabitListCreateView,
    LinkedHabitListCreateView,
    HabitListCreateView,
    HabitListView,
    HabitUpdateView,
    HabitDeleteView,
    PublicHabitListView
)


router = DefaultRouter()


app_name = HabitsConfig.name

urlpatterns = [
    path('places/create/', PlaceListCreateView.as_view(), name='place-list-create'),
    path('actions/create/', ActionListCreateView.as_view(), name='action-list-create'),
    path('pleasant-habits/create/', PleasantHabitListCreateView.as_view(), name='pleasant-habit-list-create'),
    path('linked-habits/create/', LinkedHabitListCreateView.as_view(), name='linked-habit-list-create'),
    path('habits/create/', HabitListCreateView.as_view(), name='habit-list-create'),
    path('habits/list/', HabitListView.as_view(), name='habit-list'),
    path('habits/update/<int:pk>/', HabitUpdateView.as_view(), name='habit-update'),
    path('habits/delete/<int:pk>/', HabitDeleteView.as_view(), name='lesson-delete'),
    path('habits/public/', PublicHabitListView.as_view(), name='public-habits-list'),
] + router.urls

