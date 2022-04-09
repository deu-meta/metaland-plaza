from .models import *
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        exclude = ["created_at", "modified_at"]


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comments
        exclude = ["created_at", "modified_at"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["article"] = ArticleSerializer
