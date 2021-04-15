from django import forms
from webapp.models import Tracer, Project
from django.forms import CheckboxSelectMultiple


class TracerForm(forms.ModelForm):
    class Meta:
        model = Tracer
        fields = ('surname', 'description', 'status', 'type')


class TracerDeleteForm(forms.Form):
    surname = forms.CharField(max_length=100, required=True, label='Введите название задачи, чтобы удалить её')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'start_data', 'end_data')


class ProjectDeleteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Введите название задачи, чтобы удалить её')


class ProjectUserForms(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['user']
        widget = {'user': CheckboxSelectMultiple}
