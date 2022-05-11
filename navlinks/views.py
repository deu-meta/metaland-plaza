from articles.permissions import IsStaffOrReadOnly
from django.db import transaction
from django.http import HttpRequest
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import mixins

from .models import NavLink
from .serializers import NavLinkFullSerializer, NavLinkSerializer


class NavLinkViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = NavLink.objects.all().order_by("order")
    serializer_class = NavLinkSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = None

    def create(self, request: HttpRequest, pk=None):
        serializer: NavLinkSerializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        # do ordering navlinks
        for order, navlink in enumerate(request.data):
            navlink["order"] = order

        serializer: NavLinkFullSerializer = NavLinkFullSerializer(data=request.data, many=True, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            # delete all old navlinks and replace to new navlinks
            self.queryset.delete()
            self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
