from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("lettings/", include("app_lettings.url")),
    path("profiles/", include("app_profiles.url"))
    # path("lettings/", include(("app_lettings.url", "lettings"), namespace="lettings")),
    # path("profiles/", include(("app_profiles.url", "profiles"), namespace="profiles"))
]
