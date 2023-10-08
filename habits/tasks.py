from datetime import datetime
from habits.telegram_utils import send_notification
from habits.models import Habit
from celery import shared_task


@shared_task
def remind_habits():
    current_time = datetime.now().time().replace(microsecond=0)

    for habit in Habit.objects.all():
        if current_time == habit.time:
            message = f"Не забудьте выполнить привычку: " \
                      f"{habit.action.name} " \
                      f"в {habit.time} " \
                      f"в {habit.place.name}"
            send_notification('5409971102', message)
