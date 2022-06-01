from django.db import models


class Space(models.Model):

    CATEGORY_CHOICES = [("건물", "건물"), ("학과", "학과"), ("동아리", "동아리")]

    name = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=30, choices=CATEGORY_CHOICES, null=False)
    thumbnail = models.ImageField(default="default_image.jpg")
    short_introduce = models.CharField(max_length=200, default="소개없음")
    long_introduce = models.TextField(default="글 없음")

    class Meta:
        verbose_name = "공간"
        verbose_name_plural = f"{verbose_name}"
