from django.contrib.auth import get_user_model
from django.db import models


class Notice(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False, default="제목없음")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    notion = models.CharField(max_length=400)
    viewcount = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = f"{verbose_name}"
