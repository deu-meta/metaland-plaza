from rest_framework import serializers

from .models import TokenUser


class TokenUserSerializer(serializers.ReadOnlyField):
    def to_representation(self, value: TokenUser):
        email = value.token.payload["email"]
        role = value.token.payload["role"]
        name = email.split("@")[0]

        return {
            "id": value.token.payload["sub"],
            "nickname": "****" + name[-3:],
            "role": role,
        }
