from django.urls import path, include
from website.views import WebsiteDetail, PortfolioList, BlogList, Portfoliodetail, Blogdetail

urlpatterns = [

    path('<int:pk>', WebsiteDetail.as_view(), name="websitedetail"),
    path('portfolio', PortfolioList.as_view(), name="portfoliolist"),
    path('portfolio/<int:pk>', Portfoliodetail.as_view(), name="portfoliodetail"),
    path('blog', BlogList.as_view(), name="bloglist"),
    path('blog/<int:pk>', Blogdetail.as_view(), name="blogdetail")
]
