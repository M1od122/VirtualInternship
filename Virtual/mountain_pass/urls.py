from .views import SubmitData, edit_object, view_statuses, get_object, edit_object_api, get_user_objects
from django.urls import path

urlpatterns = [
    path('submitData/', SubmitData.as_view(), name='submit_data'),
    path('edit/<int:object_id>/', edit_object, name='edit_object'),  # URL для редактирования объекта
    path('statuses/', view_statuses, name='view_statuses'),  # URL для просмотра статусов
    path('submitData/<int:object_id>/', get_object, name='get_object'),  # Получить объект по ID
    path('submitData/<int:object_id>/', edit_object_api, name='edit_object_api'),  # Редактировать объект
    path('submitData/', get_user_objects, name='get_user_objects'),  # Получить объекты по email
]
