from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("apps.api.auth.v1")),
    path("system/", include("apps.api.system.v1")),
    path("documents/", include("apps.api.documents.v1")),
]
