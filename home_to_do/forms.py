from django import forms
from home_to_do.models import *


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
