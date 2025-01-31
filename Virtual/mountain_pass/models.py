from django.db import models

class MountainPass(models.Model):
    # Определяем возможные статусы перевалов
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=255)                       # Название перевала
    coordinates = models.CharField(max_length=100)               # Координаты перевала
    height = models.IntegerField()                                # Высота перевала
    photos = models.TextField()                                   # Ссылки на фотографии
    user_name = models.CharField(max_length=255)                 # Имя пользователя
    user_email = models.EmailField()                              # Email пользователя
    user_phone = models.CharField(max_length=20)                 # Телефон пользователя
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')  # Статус перевала

    def __str__(self):
        return self.name
