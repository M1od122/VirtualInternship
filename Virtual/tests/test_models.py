# tests/test_models.py
from django.test import TestCase
from .models import MountainPass  # Импортируем модель
from django.contrib.auth.models import User  # Импортируем модель пользователя

class MountainPassModelTest(TestCase):
    def setUp(self):
        # Создать пользователя для тестирования
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Создать объект MountainPass
        self.mountain_pass = MountainPass.objects.create(
            name="Test Mountain",
            email="test@example.com",
            phone_number="1234567890",
            address="123 Test St",
            user=self.user
        )

    def test_string_representation(self):
        # Проверка строкового представления объекта MountainPass
        self.assertEqual(str(self.mountain_pass), "Test Mountain")

    def test_mountain_pass_creation(self):
        # Проверка данных созданного объекта
        self.assertEqual(self.mountain_pass.name, "Test Mountain")
        self.assertEqual(self.mountain_pass.email, "test@example.com")
        self.assertEqual(self.mountain_pass.phone_number, "1234567890")
        self.assertEqual(self.mountain_pass.address, "123 Test St")
        self.assertEqual(self.mountain_pass.user, self.user)