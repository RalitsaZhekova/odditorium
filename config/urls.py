from django.urls import include, path
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("common.urls")),
    path("collections/", include("galleries.urls")),
    path("inventions/", include("inventions.urls")),
        path("tours/", include("tours.urls"))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
