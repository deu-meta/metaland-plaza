from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Articles(models.Model):
    Q = "QA"
    F = "F"

    CATEGORY_CHOICES = [(Q, "Q&A게시판"), (F, "자유게시판")]

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200, default="제목없음")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    contents = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def is_upperclass(self):
        return self.category in (self.Q, self.F)


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Articles, related_name="articles", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    contents = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
