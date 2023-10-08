from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'time',
                    'action', 'pleasant_habit',
                    'linked_habit', 'frequency',
                    'estimated_time', 'is_public',
                    'is_completed', 'last_completed')

    def __str__(self):
        return self.name
