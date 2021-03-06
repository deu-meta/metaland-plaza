from django.db import models
from metaland.models import Authorable


class Notice(Authorable):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False, default="제목없음")
    created_at = models.DateTimeField(auto_now_add=True)
    notion = models.CharField(max_length=400)
    viewcount = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = f"{verbose_name}"
        ordering = ["-id"]
