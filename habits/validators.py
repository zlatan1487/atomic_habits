from rest_framework import serializers
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone


def validate_estimated_time(time):
    """
    Проверяет, что время выполнения не больше 120 секунд.
    """
    if int(time) > 120:
        raise serializers.ValidationError(
            "Время выполнения не должно превышать 120 секунд."
        )


def validate_linked_habit_is_pleasurable(linked_habit):
    """
       Проверяет, является ли связанная привычка приятной.
       :param linked_habit: Связанная привычка,
       которую необходимо проверить.
       :type linked_habit: LinkedHabit or None
       :raises serializers.ValidationError:
       Если связанная привычка не является приятной.
    """
    if linked_habit:
        if not linked_habit.is_pleasurable:
            raise serializers.ValidationError(
                "Связанная привычка должна быть приятной привычкой.")


def validate_reward_and_linked_habit(data):
    """
    Проверяет, что не выбрано одновременно и вознаграждение,
    и связанная привычка.
    """
    has_reward = data.get('reward')
    linked_habit = data.get('linked_habit')

    if has_reward and linked_habit:
        raise serializers.ValidationError(
            "Выберите либо вознаграждение, "
            "либо связанную привычку, но не оба.")


def validate_pleasant_habit(data):
    reward = data.get('reward')
    linked_habit = data.get('linked_habit')
    if reward is not None or linked_habit is not None:
        raise serializers.ValidationError(
            "У Приятной привычке не может быть ни вознаграждения, "
            "ни связанной привычки.")


def validate_execution_frequency(data):
    frequency = data.get('frequency')
    last_completed = data.get('last_completed')

    if frequency and last_completed:
        time_difference = timezone.now() - last_completed

        if time_difference < timedelta(days=7):
            raise ValidationError(
                "Привычку нельзя выполнять реже, "
                "чем 1 раз в 7 дней.")
