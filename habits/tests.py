
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from habits.models import Habit, Place, Action, PleasantHabit, LinkedHabit
from rest_framework_simplejwt.tokens import RefreshToken


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )

        self.place = Place.objects.create(name="Some Place")
        self.action = Action.objects.create(name="Some Action")
        self.pleasant_habit = PleasantHabit.objects.create(
            description="Some Pleasant Habit")

        self.habit_data = {
            "place": self.place.id,
            "time": "14:58:00.260081",
            "action": self.action.id,
            "pleasant_habit": self.pleasant_habit.id,
            "frequency": 1,
            "estimated_time": 110,
            "is_public": True
        }

    def test_create_habit(self):
        """
        Test habit creation.
        """

        url = reverse('habits:habit-create')

        response = self.client.post(
            url, self.habit_data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.filter(place=self.place).exists())


class PlaceAPITestCase(APITestCase):
    def setUp(self):
        # Создаем пользователя и получаем токен
        self.user = User.objects.create(
            username='testuser',
            password='testpassword')
        self.token = str(
            RefreshToken.for_user(self.user).access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_place(self):
        """
        Тест создания места
        """
        url = reverse('habits:places')
        data = {"name": "Some Place"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Place.objects.filter(name='Some Place').exists())


class PleasantHabitAPITestCase(APITestCase):
    def setUp(self):
        # Создаем пользователя и получаем токен
        self.user = User.objects.create(
            username='testuser',
            password='testpassword')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_pleasant_habit(self):
        """
        Тест создания приятной привычки
        """
        url = reverse('habits:pleasants')
        data = {"description": "Some Pleasant Habit"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(PleasantHabit.objects.filter(
            description='Some Pleasant Habit').exists())


class LinkedHabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='testpassword')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_linked_habit(self):
        """
        Тест создания связанной привычки
        """
        url = reverse('habits:linkeds')
        data = {"description": "Some Linked Habit", "is_pleasurable": True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(LinkedHabit.objects.filter(
            description='Some Linked Habit').exists())
