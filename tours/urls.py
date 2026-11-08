from django.urls import path

from tours.views import TourCreateView, TourDetailView, TourListView, TourUpdateView, tour_delete

app_name = "tours"

urlpatterns = [
    path("", TourListView.as_view(), name="tour-list"),
    path("create/", TourCreateView.as_view(), name="tour-create"),
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
