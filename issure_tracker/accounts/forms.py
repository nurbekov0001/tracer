from django import forms
from django.contrib.auth.models import User


class MyUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput, strip=False)
    email = forms.CharField(required=True)
    last_name = forms.CharField(label="last_name", strip=False, required=False)
    first_name = forms.CharField(label="first_name", required=False, strip=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        if last_name == "" and first_name == "" :
            raise forms.ValidationError('Хотябы last_name или first_name должно быть заполнено  ')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']