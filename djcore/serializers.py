from djcore.backends import authenticate
from rest_framework import serializers
from rest_framework import exceptions
from djcore.models import User
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
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
                        raise serializers.ValidationError(msg)


                    payload = jwt_payload_handler(user)


                    return {
                        'token': jwt_encode_handler(payload),
                        }
                except :
                    raise serializers.ValidationError(user)

            else:
                msg = 'Unable to login with provided credentials.'
                raise exceptions.AuthenticationFailed(msg)
        else:
            msg = 'Must include "username" and "password"'
            raise serializers.ValidationError(msg)
