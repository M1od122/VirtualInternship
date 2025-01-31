from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MountainPass
from .serializers import MountainPassSerializer

class SubmitData(APIView):
    def post(self, request):
        # Используем сериализатор для валидации и сохранения данных
        serializer = MountainPassSerializer(data=request.data)
        if serializer.is_valid():
            # Если данные валидны, сохраняем их и возвращаем успешный ответ
            mountain_pass = serializer.save()
            return Response({
                'status': 200,
                'message': 'Отправлено успешно',
                'id': mountain_pass.id  # Возвращаем ID нового объекта
            }, status=status.HTTP_200_OK)

        # Если данные не валидны, возвращаем сообщение об ошибке
        return Response({
            'status': 400,
            'message': 'Недостаточно полей'
        }, status=status.HTTP_400_BAD_REQUEST)
