from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from .models import MountainPass
from .serializers import MountainPassSerializer


class MountainPassAPITests(TestCase):
    def setUp(self):
        # Создаем клиент для тестирования API
        self.client = APIClient()
        # Создаем тестовый объект перевала
        self.mountain_pass = MountainPass.objects.create(
            name='Тестовый перевал',
            coordinates='45.0, 73.0',
            height=2500
        )

    def test_create_mountain_pass(self):
        # Регистрация нового перевала
        url = reverse('submit_data')  # Убедитесь, что название маршрута совпадает
        data = {
            'name': 'Новый перевал',
            'coordinates': '46.0, 74.0',
            'height': 3000,
            'user_name': 'Тестовый пользователь',
            'user_email': 'test@example.com',
            'user_phone': '1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MountainPass.objects.count(), 2)

    def test_update_mountain_pass(self):
        # Обновление существующего перевала
        url = reverse('submit_data', kwargs={'pk': self.mountain_pass.pk})  # Используйте правильный путь
        data = {
            'name': 'Обновленный перевал',
            'height': 2600
        }
        response = self.client.put(url, data, format='json')
        self.mountain_pass.refresh_from_db()  # Обновляем объект из базы данных
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.mountain_pass.name, 'Обновленный перевал')
        self.assertEqual(self.mountain_pass.height, 2600)

    def test_get_mountain_pass(self):
        # Получение информации о перевале
        url = reverse('submit_data', kwargs={'pk': self.mountain_pass.pk})  # Используйте правильный путь
        response = self.client.get(url)
        serializer = MountainPassSerializer(self.mountain_pass)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_mountain_pass(self):
        # Удаление перевала
        url = reverse('submit_data', kwargs={'pk': self.mountain_pass.pk})  # Используйте правильный путь
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MountainPass.objects.count(), 0)