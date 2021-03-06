from django.db import models
from metaland.models import Authorable


# Create your models here.
class Article(Authorable):
    Q = "QA"
    F = "F"

    CATEGORY_CHOICES = [(Q, "Q&A게시판"), (F, "자유게시판")]

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200, default="제목없음")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    contents = models.TextField()

    def is_upperclass(self):
        return self.category in (self.Q, self.F)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "게시물"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["-id"]


class Comment(Authorable):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, related_name="articles", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    contents = models.TextField()

    def __str__(self):
        return "{}에 댓글 {}번".format(self.article, self.id)

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["id"]
