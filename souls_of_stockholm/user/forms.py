from django import forms
from souls_of_stockholm.user.models import CustomUser


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        label_suffix='',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Имя пользователя',
                                     'required': 'required'})
    )
    password = forms.CharField(
        label='Пароль',
        label_suffix='',
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Пароль',
                                          'required': 'required'
                                          })
    )
    confirm_password = forms.CharField(
        label='Подтверждение пароля',
        label_suffix='',
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Подтверждение пароля',
                                          'required': 'required'
                                          })
    )
    age = forms.IntegerField(
        label='Возраст',
        label_suffix='',
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                          'placeholder': 'Возраст',
                                          'required': 'required'
                                          })
    )
    gender = forms.ChoiceField(
        label='Пол',
        label_suffix='',
        choices=(('male', "Мужской"), ('female', "Женский"), ('other', "Другой")),
        widget=forms.Select(attrs={'class': 'form-control',
                                         'required': 'required'
                                         })
        )
    country = forms.CharField(
        label='Страна',
        label_suffix='',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                         'placeholder': 'Страна',
                                         'required': 'required'
                                         })
    )

