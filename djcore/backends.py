from djcore.models import User
from rest_framework import exceptions

def authenticate(username=None, password=None, **kwargs):
    try:
        user = User.objects.get(email=username)

        if user.check_password(password):
            return user
        else:
            return exceptions.AuthenticationFailed('incorrect password')
    except User.DoesNotExist:
        return exceptions.AuthenticationFailed('User does not exist.')