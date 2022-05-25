from functools import cached_property

from django.db import models
from rest_framework_simplejwt.models import TokenUser as BaseTokenUser


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

