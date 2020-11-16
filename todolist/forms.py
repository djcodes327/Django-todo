from django import forms
from todolist.models import tasklist


class taskfrom(forms.ModelForm):
    class Meta:
        model = tasklist
        fields = ['task', 'done']
