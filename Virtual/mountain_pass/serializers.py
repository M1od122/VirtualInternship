from rest_framework import serializers
from .models import MountainPass

class MountainPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainPass  # Определяем модель
        fields = [
            'id',
            'name',
            'coordinates',
            'height',
            'photos',
            'user_name',
            'user_email',
            'user_phone',
            'status'
        ]

    def update(self, instance, validated_data):
        """
        Переопределяем метод update для обработки данных
        при обновлении объекта модели MountainPass.
        """
        # Обновляем поля экземпляра модели с валидацией данных
        instance.name = validated_data.get('name', instance.name)
        instance.coordinates = validated_data.get('coordinates', instance.coordinates)
        instance.height = validated_data.get('height', instance.height)
        instance.photos = validated_data.get('photos', instance.photos)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.user_phone = validated_data.get('user_phone', instance.user_phone)
        instance.status = validated_data.get('status', instance.status)

        # Сохраняем обновленный объект в базе данных
        instance.save()

        return instance