from django.contrib import admin
from .models import MountainPass

@admin.register(MountainPass)
class MountainPassAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinates', 'height')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)
