from rest_framework import serializers

from .models import Notice


class NoticeSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="user.nickname")

    class Meta:
        model = Notice
        fields = ["id", "title", "notion", "author"]
