from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shahid.urls", namespace="shahid")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
