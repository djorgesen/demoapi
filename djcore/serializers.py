from djcore.backends import authenticate
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework_jwt.settings import api_settings
from datetime import datetime
import jwt

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class JSONWebTokenSerializer(serializers.Serializer):
    """
    Serializer class used to validate a username and password.

    Returns a JSON Web Token that can be used to authenticate later calls.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')



        if username and password:
            user = authenticate(username, password)

            if user:
                try:
                    if not user.is_active:
                        msg = 'User account is disabled.'
                        raise exceptions.AuthenticationFailed(msg)


                    payload = jwt_payload_handler(user)


                    return {
                        'token': jwt_encode_handler(payload),
                        }
                except :
                    raise exceptions.AuthenticationFailed(user)

            else:
                msg = 'Unable to login with provided credentials.'
                raise exceptions.AuthenticationFailed(msg)
        else:
            msg = 'Must include "username" and "password"'
            raise exceptions.AuthenticationFailed(msg)


def jwt_payload_handler(user):
    return {
        'user_id': user.pk,
        'email': user.email,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }