from django import forms
from souls_of_stockholm.user.models import CustomUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'age', 'gender', 'country']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Имя пользователя',
                                               'required': 'required'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Пароль',
                                                   'required': 'required'
                                                   }),
            'age': forms.NumberInput(attrs={'class': 'form-control',
                                            'placeholder': 'Возраст',
                                            'required': 'required'
                                            }),
            'gender': forms.Select(attrs={'class': 'form-control',
                                          'required': 'required'
                                          }),
            'country': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Страна',
                                              'required': 'required'
                                              }),
        }
        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль',
            'age': 'Возраст',
            'gender': 'Пол',
            'country': 'Страна'
        }

    confirm_password = forms.CharField(
        label='Подтверждение пароля',
        label_suffix='',
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Подтверждение пароля',
                                          'required': 'required'
                                          })
    )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.choices = [('male', "Мужской"),
                                                ('female', "Женский"),
                                                ('other', "Другой")]
