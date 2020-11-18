from crispy_forms.helper import FormHelper
from django.contrib.admin.helpers import Fieldset
from django.forms import ModelForm, DateInput
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .models import body_stats_tbl


# Renders the database table as a form that can be used in the html page
class bodyStatsForm(ModelForm):
    class Meta:
        model = body_stats_tbl

        widgets = {
            'bs_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }

        fields = ('bs_date', 'height', 'weight', 'bmi')

    # init initialises the form, self accesses attributes of the class
    def __init__(self, *args, **kwargs):
        super(bodyStatsForm, self).__init__(*args, **kwargs)
        self.fields['bs_date'].input_formats = ('%Y-%m-%dT%H:%M',)