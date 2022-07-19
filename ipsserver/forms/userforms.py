from django import forms
from django.forms import models

from ipsserver.models import Department, UserInfo


class UserModelForm(forms.ModelForm):

    name = forms.CharField(min_length=3, max_length=15, label='用户名')

    class Meta:
        model = UserInfo
        fields = ["name", 'age', 'account', 'create_time', 'gender', 'depart']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
