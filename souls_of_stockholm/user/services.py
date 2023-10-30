from souls_of_stockholm.user.validator import check_password, check_len_password


def check_errors(password1, password2):
    if not check_password(password1, password2):
        return 'Пароли не совпадают'
    elif not check_len_password(password1):
        return 'Пароль слишком короткий'
