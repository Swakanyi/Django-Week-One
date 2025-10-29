from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import FoodItem
from .forms import FoodItemForm
from django.contrib import messages
from django.utils import timezone

# Create your views here.


def index(request):
    
    today_foods = FoodItem.objects.filter(created_at__date=timezone.now().date())
    total_calories = FoodItem.get_total_calories_today()
    
    context = {
        'food_items': today_foods,
        'total_calories': total_calories,
        'today': timezone.now().date(),
    }
    return render(request, 'index.html', context)


def add_food(request):
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food item added successfully!')
            return redirect('index')
    else:
        form = FoodItemForm()
    
    return render(request, 'add_food.html', {'form': form})


def delete_food(request, food_id):

    food_item = get_object_or_404(FoodItem, id=food_id)
    
    if request.method == 'POST':
        food_item.delete()
        messages.success(request, 'Food item deleted successfully!')
        return redirect('index')
    
    
    return render(request, 'delete_food.html', {'food_item': food_item})


def reset_calories(request):
    
    if request.method == 'POST':
        deleted_count = FoodItem.reset_today_calories()
        messages.success(request, f'Reset {deleted_count} food items!')
        return redirect('index')
    
    return render(request, 'reset_calories.html')


def food_list(request):
   
    all_foods = FoodItem.objects.all()
    return render(request, 'food_list.html', {'food_items': all_foods})
