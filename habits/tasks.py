from datetime import datetime, time, timedelta
from habits.telegram_utils import send_notification  # Импортируйте вашу функцию отправки уведомлений
from habits.models import Habit
from django.utils import timezone
from celery import shared_task


@shared_task
def remind_habits():
    current_time = datetime.now().time().replace(microsecond=0)

    for habit in Habit.objects.all():
        if current_time == habit.time:
            message = f"Не забудьте выполнить привычку: {habit.action.name} в {habit.time} в {habit.place.name}"
            send_notification('5409971102', message)

