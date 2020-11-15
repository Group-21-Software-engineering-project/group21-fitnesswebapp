from django.forms import ModelForm, DateInput
from .models import exerciseLog

#renders the database table as a form that can be used in the html page
class ExerciseForm(ModelForm):
    class Meta:
        model = exerciseLog

        widgets = {
            'day': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }

        fields = ('day', 'hours', 'minutes', 'exercise_type', 'notes'
        )

    #init initalizes the form, self accesses attributes of the class.
    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.fields['day'].input_formats = ('%Y-%m-%dT%H:%M',)