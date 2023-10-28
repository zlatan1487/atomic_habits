from datetime import datetime, timezone, timedelta
from django.utils import timezone
from habits.telegram_utils import send_message_to_user
from users.models import User
from habits.models import Habit
from celery import shared_task
import pytz


@shared_task
def remind_habits():
    current_time = datetime.now().time()
    time_interval = datetime.now() - timedelta(minutes=1)
    habits = Habit.objects.filter(time__gte=time_interval)
    print('habits----------', habits)
    for habit in habits.filter(time__lte=current_time):
        print("habit", habit.time)
        print('Executing remind_habits for habit.id:', habit.id)
        sendhabit_notification.delay(habit.id)


@shared_task
def sendhabit_notification(habit_id):
    try:
        print('habit_id', habit_id)
        habit = Habit.objects.get(pk=habit_id)
        user = User.objects.get(id=habit.user_id)

        message = f"Не забудьте выполнить привычку: " \
                  f"{habit.action.name} " \
                  f"в {habit.time} " \
                  f"в {habit.place.name}"
        send_message_to_user(user.chat_id, message)
        print('Notification sent successfully.')
    except Exception as e:
        print('Error sending notification:', str(e))

