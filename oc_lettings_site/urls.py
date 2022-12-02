from django.contrib import admin
from django.urls import path, include

from .views import index


class SentryTestError(Exception):
    pass


def raise_error(*args, **kwargs):
    raise SentryTestError("Test error for Sentry")


urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("lettings/", include("app_lettings.url")),
    path("profiles/", include("app_profiles.url")),
    path("sentry-debug/", raise_error)
    # path("lettings/", include(("app_lettings.url", "lettings"), namespace="lettings")),
    # path("profiles/", include(("app_profiles.url", "profiles"), namespace="profiles"))
]
