# tests/test_views.py
from django.test import TestCase
from django.urls import reverse  # Импортируем для создания URL
from .models import MountainPass  # Импортируем модель
from django.contrib.auth.models import User  # Импортируем для создания пользователей
from rest_framework import status  # Импортируем статус для проверки
from rest_framework.test import APIClient  # Импортируем клиент API для тестирования


class MountainPassAPITest(TestCase):
    def setUp(self):
        # Создание пользователя для авторизации в тестах
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()  # Создаем экземпляр клиента API
        self.client.force_authenticate(user=self.user)  # Принудительная аутентификация пользователя

        # Создание объекта MountainPass для тестов
        self.mountain_pass = MountainPass.objects.create(
            name="Test Mountain",
            email="test@example.com",
            phone_number="1234567890",
            address="123 Test St",
            user=self.user
        )

    def test_edit_and_fetch_object(self):
        # Редактируем объект
        response = self.client.patch(
            reverse('edit_object_api', args=[self.mountain_pass.id]),
            {
                'name': 'Updated Mountain',
                'address': '321 Updated St'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверяем, что статус ответа 200

        # Получаем объект для проверки изменений
        response = self.client.get(reverse('get_object', args=[self.mountain_pass.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверяем, что статус ответа 200
        self.assertEqual(response.data['name'], 'Updated Mountain')  # Проверяем обновленное имя
        self.assertEqual(response.data['address'], '321 Updated St')  # Проверяем обновленный адрес

    def test_create_and_fetch_object(self):
        # Создаем новый объект через API
        response = self.client.post(reverse('edit_object_api'), {
            'name': 'New Mountain',
            'email': 'new@example.com',
            'phone_number': '0987654321',
            'address': '456 New St'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверяем, что статус 201

        new_pass_id = response.data['id']  # Получаем ID нового объекта

        # Проверяем, что новый объект создан правильно
        response = self.client.get(reverse('get_object', args=[new_pass_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверяем, что статус ответа 200
        self.assertEqual(response.data['name'], 'New Mountain')  # Проверяем имя нового объекта
        self.assertEqual(response.data['email'], 'new@example.com')  # Проверяем email
        self.assertEqual(response.data['phone_number'], '0987654321')  # Проверяем номер телефона
        self.assertEqual(response.data['address'], '456 New St')  # Проверяем адрес