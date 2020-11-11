from django.forms import ModelForm, DateInput
from .models import exerciseLog

class ExerciseForm(ModelForm):
    class Meta:
        model = exerciseLog

        widgets = {
            'day': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.fields['day'].input_formats = ('%Y-%m-%dT%H:%M',)