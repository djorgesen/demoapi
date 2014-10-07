from vocore.models import User

def authenticate(username=None, password=None, **kwargs):
    try:
        user = User.objects.get(email=username)

        if user.check_password(password):
            return user
    except User.DoesNotExist:
        return 'User does not Exist.'


