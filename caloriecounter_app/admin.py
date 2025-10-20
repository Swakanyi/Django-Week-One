from django.contrib import admin
from .models import FoodItem

# Register your models here.
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    ordering = ['-created_at']