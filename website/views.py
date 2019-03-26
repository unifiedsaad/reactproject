from django.shortcuts import render

from .models import Website
from website.serializers import WebsiteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class WebsiteDetail(generics.RetrieveAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = []