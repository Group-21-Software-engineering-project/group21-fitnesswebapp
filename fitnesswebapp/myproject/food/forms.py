from django.forms import ModelForm, DateInput
from .models import food_tbl


# Renders the database table as a form that can be used in the html page
class foodForm(ModelForm):
    class Meta:
        model = food_tbl

        widgets = {
            'food_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }

        fields = (
        'food_date', 'food_name', 'food_calories', 'food_weight', 'food_fat', 'food_protein', 'food_carbohydrates')

    # init initialises the form, self accesses attributes of the class
    def __init__(self, *args, **kwargs):
        super(foodForm, self).__init__(*args, **kwargs)
        self.fields['food_date'].input_formats = ('%Y-%m-%dT%H:%M',)
