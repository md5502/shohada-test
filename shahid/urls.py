from django.urls import path

from .views import shahid_detail, shahid_list

app_name = "shahid"

urlpatterns = [
    path("", shahid_list, name="shahid_list"),
    path("<str:slug>/", shahid_detail, name="shahid_detail"),
]
