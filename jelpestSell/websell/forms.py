from django.forms import fields
from django.forms.models import ModelForm
from .models import Demo
from django import forms


class DemoForm(ModelForm):
    class Meta:
        model = Demo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['style'] = 'margin-bottom: 2rem'