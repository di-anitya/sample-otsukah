from django import forms
from .models import Driver, Physical, Virtual
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class DriverForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    class Meta:
        model = Driver
        fields = ('name', 'plugin')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'AWS Drivers'}),
            'plugin': forms.TextInput(attrs={'placeholder':'boto3'}),
        }


class PhysicalForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    class Meta:
        model = Physical
        fields = ('name', 'category', 'driver_id', 'ip_address', 'access_key', 'secret_key', 'az', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'AWS (Tokyo Region)'}),
            'category': forms.TextInput(attrs={'placeholder':'AWS'}),
            # 'driver_id': forms.Select(choices=DRIVER_CHOICES)
            'ip_address': forms.TextInput(attrs={'placeholder':'192.168.0.114'}),
            'access_key': forms.TextInput(attrs={'placeholder':'PBA2DBENZ2NFM9J2M6Q8'}),
            'secret_key': forms.TextInput(attrs={'placeholder':'CyPJJ5zCAWubnbgCXafUBkB63sWiQTyyQWQJ99FW'}),
            'az': forms.TextInput(attrs={'placeholder':'ap-northeast-1'}),
            'description': forms.Textarea(attrs={'placeholder':'AWS'}),
        }


class VirtualForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    class Meta:
        model = Virtual
        fields = ('name', 'physical_id', 'tags', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'aws-vm01'}),
            'tags': forms.TextInput(attrs={'placeholder':'EC2'}),
            'description': forms.Textarea(attrs={'placeholder':'Webサーバ用インスタンス'}),
        }
