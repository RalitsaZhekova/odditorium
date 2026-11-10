from django.urls import path

from tours.views import TourCreateView, TourDetailView, TourListView, TourUpdateView, tour_builder, tour_delete, tour_preview_save

app_name = "tours"

urlpatterns = [
    path("", TourListView.as_view(), name="tour-list"),
    path("create/", TourCreateView.as_view(), name="tour-create"),
    path("surprise/", tour_builder, name="tour-builder"),
    path("surprise/save/", tour_preview_save, name="tour-preview-save"),
    path("<int:pk>/", TourDetailView.as_view(), name="tour-detail"),
    path(
        "<int:pk>/edit/",
        TourUpdateView.as_view(),
        name="tour-edit"
    ),
    path(
        "<int:pk>/delete/",
        tour_delete,
        name="tour-delete"
    )
]
