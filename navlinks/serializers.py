from rest_framework import serializers

from .models import NavLink


class NavLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavLink
        fields = ["name", "link"]


class NavLinkFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavLink
        fields = "__all__"
