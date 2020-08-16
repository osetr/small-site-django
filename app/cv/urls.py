from django.urls import path
from .views import *

urlpatterns = [
    path("add/", AddPost.as_view(), name="main"),
    path("show/", ShowPosts.as_view(), name="show"),
]
