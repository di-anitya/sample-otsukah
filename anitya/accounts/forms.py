from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
