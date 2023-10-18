def check_password(passwd1, passwd2):
    if passwd1 != passwd2:
        return False
    return True


def check_len_password(passwd):
    if len(passwd)<8:
        return False
    return True