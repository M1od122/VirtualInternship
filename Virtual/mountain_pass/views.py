from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MountainPass
from .forms import MountainPassForm
from .serializers import MountainPassSerializer
import json

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

def edit_object(request, object_id):
    # Получаем объект по ID и проверяем, принадлежит ли он текущему пользователю
    mountain_pass = get_object_or_404(MountainPass, id=object_id, user=request.user)

    # Проверяем, можно ли редактировать объект
    if mountain_pass.status != 'new':
        return render(request, 'error.html', {'message': 'Редактирование невозможно, так как статус не новый.'})

    if request.method == 'POST':
        form = MountainPassForm(request.POST, instance=mountain_pass)  # Создаем форму с данными объекта
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('success_url')  # Замените на нужный URL
    else:
        form = MountainPassForm(instance=mountain_pass)  # Если не POST, создаем форму с текущими данными

    return render(request, 'edit_object.html', {'form': form})  # Отправляем форму в шаблон

def view_statuses(request):
    # Получаем все объекты текущего пользователя
    mountain_passes = MountainPass.objects.filter(user=request.user)
    return render(request, 'view_statuses.html', {'user_objects': mountain_passes})  # Отправляем объекты в шаблон

@api_view(['GET'])
def get_object(request, object_id):
    """Получить одну запись по её ID."""
    mountain_pass = get_object_or_404(MountainPass, id=object_id)
    data = {
        'name': mountain_pass.name,
        'email': mountain_pass.email,
        'phone_number': mountain_pass.phone_number,
        'address': mountain_pass.address,
        'status': mountain_pass.status,
    }
    return JsonResponse(data)  # Возвращаем данные объекта в формате JSON

@api_view(['PATCH'])
def edit_object_api(request, object_id):
    """Редактировать существующую запись, если она в статусе new."""
    mountain_pass = get_object_or_404(MountainPass, id=object_id)

    # Проверяем, можно ли редактировать объект
    if mountain_pass.status != 'new':
        return JsonResponse({
            'state': 0,
            'message': 'Редактирование невозможно, так как статус не новый.'
        })

    try:
        data = json.loads(request.body)  # Загружаем данные из тела запроса
        # Обновляем только разрешенные поля
        mountain_pass.name = data.get('name', mountain_pass.name)
        mountain_pass.address = data.get('address', mountain_pass.address)
        mountain_pass.save()  # Сохраняем изменения
        return JsonResponse({'state': 1})  # Возвращаем успешный ответ
    except Exception as e:
        return JsonResponse({
            'state': 0,
            'message': str(e)  # Возвращаем сообщение об ошибке
        })

@api_view(['GET'])
def get_user_objects(request):
    """Получить список объектов, отправленных пользователем с указанным email."""
    email = request.GET.get('user__email')  # Получаем email из параметров запроса
    mountain_passes = MountainPass.objects.filter(email=email)  # Фильтруем объекты по email
    # Составляем список объектов для возврата
    data = [{'id': obj.id, 'name': obj.name, 'status': obj.status} for obj in mountain_passes]
    return JsonResponse(data, safe=False)  # Возвращаем список объектов в формате JSON