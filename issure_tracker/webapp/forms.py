from django import forms
from webapp.models import Tracer, Status, Type


class TracerForm(forms.ModelForm):
    class Meta:
        model = Tracer
        fields = ('surname', 'description', 'status', 'type')


class TracerDeleteForm(forms.Form):
    surname = forms.CharField(max_length=100, required=True, label='Введите название задачи, чтобы удалить её')
