from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import Demo
from django import forms


class DemoForm(ModelForm):
    day = forms.DateTimeField(label="Día", input_formats=['%d/%m/%Y'], widget=forms.DateTimeInput(attrs={'type': 'date'}))
    hour = forms.DateTimeField(label="Hora", input_formats=['%H:%M:%S'], widget=forms.DateTimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Demo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-4'