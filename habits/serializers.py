from rest_framework import serializers
from habits.models import Place, Action, PleasantHabit, LinkedHabit, Habit
from habits.validators import (
    validate_estimated_time,
    validate_linked_habit_is_pleasurable,
    validate_reward_and_linked_habit,
    validate_pleasant_habit,
    validate_execution_frequency
)


class PlaceSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Place.
    """
    class Meta:
        model = Place
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Action.
    """
    class Meta:
        model = Action
        fields = '__all__'


class PleasantHabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели PleasantHabit.
    """
    class Meta:
        model = PleasantHabit
        fields = '__all__'


class LinkedHabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели LinkedHabit.
    """
    class Meta:
        model = LinkedHabit
        fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.
    """
    estimated_time = serializers.CharField(
        validators=[validate_estimated_time]
    )

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        linked_habit = data.get('linked_habit')
        validate_linked_habit_is_pleasurable(linked_habit)
        validate_reward_and_linked_habit(data)
        validate_pleasant_habit(data)
        validate_execution_frequency(data)

        return data
