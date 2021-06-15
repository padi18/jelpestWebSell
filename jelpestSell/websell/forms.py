from datetime import date
from .models import Demo
from django import forms


class DemoForm(forms.ModelForm):

    class Meta:
        model = Demo
        fields = '__all__'
        widgets = {
            'day' : forms.DateInput(attrs={'type': 'date', 'min': date.today()}),
            'hour' : forms.TimeInput(attrs={'type': 'time', 'min': '08:00', 'max': '20:00'})
        }

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-4'