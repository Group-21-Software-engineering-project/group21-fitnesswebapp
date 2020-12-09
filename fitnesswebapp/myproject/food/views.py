from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import food_tbl
from django.shortcuts import render, redirect
from .forms import foodForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def foodUpload(request):
    return render(request, 'food/foodUpload.html')


def foodView(request):
    return render(request, 'food/foodView.html')


# allow user to upload their food to the database table
@login_required  # users have to be logged in to access the food upload page
def upload_food(request, upload_food_id=None):
    if upload_food_id:
        instance = get_object_or_404(foodForm, pk=upload_food_id)
    else:
        instance = food_tbl()

    form = foodForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        your_object = form.save(commit=False)
        your_object.user = request.user
        your_object.save()
        messages.success(request, f'Food has been uploaded')
        return redirect('foodUpload-page')
    return render(request, 'food/foodUpload.html', {'form': form})


@login_required  # users have to be logged in to access the body stats view page
def view_food(request):
    data = food_tbl.objects.values_list('food_date', 'food_name', 'food_calories', 'food_weight', 'food_fat', 'food_protein', 'food_carbohydrates', 'user')  # create a variable as an object made up of all of the attributes that are stated
    food = {
        'data': data
    }
    return render(request, 'food/foodView.html', food)



