from django import forms
from .models import Driver
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class DriverForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    class Meta:
        model = Driver
        fields = ('name','plugin')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'記入例：AWS Drivers'}),
            'plugin': forms.TextInput(attrs={'placeholder':'記入例：boto3'}),
        }
