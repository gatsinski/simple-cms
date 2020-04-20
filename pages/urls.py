from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.PageRedirectView.as_view(), name="home"),
    path("404/", views.NotFoundView.as_view(), name="not_found"),
    re_path("^", views.PageView.as_view(), name="standard_page"),
]
