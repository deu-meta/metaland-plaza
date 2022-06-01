from functools import cached_property

from django.db import models
from rest_framework_simplejwt.models import TokenUser as BaseTokenUser

from .tokens import StaleToken

ROLE_PERMISSIONS = {
    "default": [],
    "student": [],
    "staff": ["staff"],
    "admin": ["staff", "admin"],
}


class TokenUser(BaseTokenUser):
    @cached_property
    def id(self):
        return self.token.get("sub")

    @cached_property
    def role(self):
        return self.token.get("role", "default")

    @cached_property
    def is_staff(self):
        return "staff" in ROLE_PERMISSIONS[self.role]

    @cached_property
    def is_superuser(self):
        return "admin" in ROLE_PERMISSIONS[self.role]

    def __getattr__(self, attr):
        value = super().__getattr__(attr)
        if value is None:
            raise AttributeError(f"{attr} is not exists")

        return value


class TokenUserField(models.JSONField):
    """
    JWT Token으로 된 유저 정보를 저장하기 위한 필드.
    iat, nbf, jti와 같은 불필요한 데이터들을 제외하고 display_name, email, given_name과 같은 핵심 데이터만 저장한다.
    """

    # 커스텀 Field 정의
    # https://docs.djangoproject.com/ko/4.0/howto/custom-model-fields/

    clean_keys = ["iat", "nbf", "jti", "exp", "type", "fresh"]
    """JWT Payload에서 사용하지 않을 필드들"""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def from_db_value(self, value, expression, connection):
        value = super().from_db_value(value, expression, connection)
        if value is None:
            return value

        if not isinstance(value, dict):
            return value

        return TokenUser(StaleToken(value))

    def get_prep_value(self, value: TokenUser):
        if value is None:
            return value

        payload = dict(value.token.payload)
        for key in self.clean_keys:
            del payload[key]

        return super().get_prep_value(payload)
