
from django.urls import path, include
from website.views import WebsiteDetail

urlpatterns = [

    path('/<int:pk>', WebsiteDetail.as_view(), name="websitedetail")
]
