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
    path('places/',
         PlaceListCreateView.as_view(),
         name='places'),
    path('actions/',
         ActionListCreateView.as_view(),
         name='actions'),
    path('pleasants/',
         PleasantHabitListCreateView.as_view(),
         name='pleasants'),
    path('linked-habits/',
         LinkedHabitListCreateView.as_view(),
         name='linked-habits'),
    path('habit/create/',
         HabitListCreateView.as_view(),
         name='habit-create'),
    path('habit/list/',
         HabitListView.as_view(),
         name='habit-list'),
    path('habit/update/<int:pk>/',
         HabitUpdateView.as_view(),
         name='habit-update'),
    path('habit/delete/<int:pk>/',
         HabitDeleteView.as_view(),
         name='lesson-delete'),
    path('habit/public/',
         PublicHabitListView.as_view(),
         name='public-habits-list'),
] + router.urls
