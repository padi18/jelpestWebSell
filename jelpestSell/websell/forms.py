from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import Demo
from django import forms


class DemoForm(ModelForm):
    date = forms.DateTimeField(label="Día y hora", input_formats=['%d/%m/%Y %H:%M:%S'], widget=forms.DateTimeInput(attrs={'id': 'datetimepicker'}))

    class Meta:
        model = Demo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control shadow-sm mb-4'