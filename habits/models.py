from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Place(models.Model):
    """
    Модель - места
    """
    name = models.CharField(max_length=255, verbose_name="Название места")


class Action(models.Model):
    """
    Модель - действия
    """
    name = models.CharField(max_length=255, verbose_name="Название действия")


class PleasantHabit(models.Model):
    """
    Модель - приятная привычка
    """
    description = models.TextField(verbose_name="Описание приятной привычки")


class LinkedHabit(models.Model):
    """
    Модель - связаная привычка
    """
    description = models.TextField(verbose_name="Описание связанной привычки")
    is_pleasurable = models.BooleanField(default=True, verbose_name="статус")


class Habit(models.Model):
    """
    Модель - привычка
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    place = models.ForeignKey(
        Place,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Место"
    )

    time = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Время выполнения"
    )

    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE,
        verbose_name="Действие"
    )

    pleasant_habit = models.ForeignKey(
        PleasantHabit,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Приятная привычка"
    )

    linked_habit = models.ForeignKey(
        LinkedHabit,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка"
    )

    frequency = models.PositiveIntegerField(
        default=1,
        verbose_name="Частота"
    )
    estimated_time = models.PositiveIntegerField(
        verbose_name="Оцененное время выполнения"
    )
    is_public = models.BooleanField(default=False, verbose_name="Публичность")
    is_completed = models.BooleanField(default=False, verbose_name="Завершено")
    last_completed = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Последнее выполнение"
    )

    def __str__(self):
        return self.action.name
