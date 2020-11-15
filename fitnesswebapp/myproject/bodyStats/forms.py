from django.forms import ModelForm, DateInput
from .models import body_stats_tbl


class bodyStatsForm(ModelForm):
    class Meta:
        model = body_stats_tbl

        widgets = {
            'bs_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }

        fields = ('bs_entry_id', 'bs_date', 'height', 'weight', 'bmi')

    def __init__(self, *args, **kwargs):
        super(bodyStatsForm, self).__init__(*args, **kwargs)
        self.fields['bs_date'].input_formats = ('%Y-%m-%dT%H:%M',)
