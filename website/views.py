from django.shortcuts import render

from .models import Website, portfolio, Blog
from website.serializers import WebsiteSerializer, PortfolioSerializer, BlogSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class WebsiteDetail(generics.RetrieveAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = []


class Portfoliodetail(generics.RetrieveAPIView):
    queryset = portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = []

class Blogdetail(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = []


class PortfolioList(generics.ListAPIView):
    queryset = portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = []


class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = []
