from django.urls import include, path

urlpatterns = [
    path("", include("common.urls")),
    path("collections/", include("galleries.urls")),
]
