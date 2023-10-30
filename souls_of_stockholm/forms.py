from django import forms


class CustomUserForm(forms.Form):
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
