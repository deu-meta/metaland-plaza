from rest_framework import serializers

from .models import Notices


class NoticeSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="user.nickname")

    class Meta:
        model = Notices
        fields = ["id", "title", "notion", "author"]
