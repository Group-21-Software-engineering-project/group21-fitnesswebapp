from django.forms import ModelForm, DateInput
from .models import food_tracker_tbl


class foodForm(ModelForm):
    class Meta:
        model = food_tracker_tbl

        widgets = {
            'food_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }

        fields = ('food_id', 'food_date', 'food_name', 'food_weight', 'food_calories', 'food_carbohydrates', 'food_protein', 'food_fat')

    def __init__(self, *args, **kwargs):
        super(foodForm, self).__init__(*args, **kwargs)
        self.fields['food_date'].input_formats = ('%Y-%m-%dT%H:%M',)
