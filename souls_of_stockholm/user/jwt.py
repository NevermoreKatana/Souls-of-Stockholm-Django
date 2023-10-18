from rest_framework_simplejwt.tokens import RefreshToken

def generate_tokens(user):
    refresh = RefreshToken.for_user(user)
    token = {
        'access': str(refresh.access_token)
    }
    return token
