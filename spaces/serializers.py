from rest_framework import serializers

from .models import Spaces


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spaces
        fields = "__all__"
