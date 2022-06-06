from metaland.serializers import TokenUserSerializer
from rest_framework import serializers

from .models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    author = TokenUserSerializer()

    class Meta:
        model = Notice
        fields = ("id", "title", "created_at", "notion", "author")
