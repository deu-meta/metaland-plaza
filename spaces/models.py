import os
import uuid

from django.conf import settings
from django.db import models


def get_image_path(instance, filename) -> str:
    return os.path.join("spaces", "{}.{}".format(uuid.uuid4(), filename.split(".")[-1]))


class Space(models.Model):

    CATEGORY_CHOICES = [("건물", "건물"), ("학과", "학과"), ("동아리", "동아리")]

    name = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=30, choices=CATEGORY_CHOICES, null=False)
    thumbnail = models.ImageField(upload_to=get_image_path, null=True)
    short_introduce = models.CharField(max_length=200, default="소개없음")
    long_introduce = models.TextField(default="글 없음")

    class Meta:
        verbose_name = "공간"
        verbose_name_plural = f"{verbose_name}"
