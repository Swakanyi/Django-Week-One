from django.db import models
from django.utils import timezone

# Create your models here.
class FoodItem(models.Model):

    name = models.CharField(max_length=200, help_text="Name of food item")
    calories= models.PositiveIntegerField(help_text="Calorie count")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.calories} calories" 

    @classmethod
    def get_total_calories_today(cls):
          today = timezone.now().date()
          today_items = cls.objects.filter(created_at__date=today)
          return sum(item.calories for item in today_items)
    
    @classmethod
    def reset_today_calories(cls):
        today = timezone.now().date()
        deleted_count, _ = cls.objects.filter(created_at__date=today).delete()
        return deleted_count