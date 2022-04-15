from django.urls import path
from .views import homepage, blog_detail, BlogList

urlpatterns = [
    path("", BlogList.as_view(), name="homepage"),
    #path("", HomepageBannerContent.as_view(), name="homepage"),
    path("blog_detail/", blog_detail, name="blog_detail"),
]
