# Create your views here.
from datetime import datetime, timedelta

from articles.permissions import IsStaffOrReadOnly
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Notice
from .serializers import NoticeSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, pk=None):
        # obj = self.get_object()
        # obj.viewcount = F("viewcount") + 1
        # obj.save(
        #     update_fields=[
        #         "viewcount",
        #     ]
        # )
        # obj.refresh_from_db()
        # serializer = self.get_serializer()
        # return Response(serializer.data, status=200)

        notice = get_object_or_404(self.get_queryset(), pk=pk)

        expire_date, now = datetime.now(), datetime.now()
        expire_date += timedelta(days=1)
        expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
        expire_date -= now
        max_age = expire_date.total_seconds()

        # response를 미리 받고 쿠키를 만들어야 한다
        serializer = self.get_serializer(notice)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        cookie_value = request.COOKIES.get("hit", "_")

        if f"_{pk}_" not in cookie_value:
            cookie_value += f"{pk}_"
            response.set_cookie("hit", value=cookie_value, max_age=max_age, httponly=True)
            with transaction.atomic():
                notice.viewcount += 1
                notice.save()

        return response
