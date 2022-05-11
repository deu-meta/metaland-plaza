from django.db import models


class NavLink(models.Model):

    name = models.CharField(max_length=20, null=False, blank=False)
    order = models.IntegerField(null=False)
    link = models.URLField(null=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.link})"

    class Meta:
        verbose_name = "네비게이션 링크"
        verbose_name_plural = f"{verbose_name}"
