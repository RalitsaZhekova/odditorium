from django.urls import path

from tours.views import TourCreateView, TourDetailView, TourListView

app_name = "tours"

urlpatterns = [
    path("", TourListView.as_view(), name="tour-list"),
    path("create/", TourCreateView.as_view(), name="tour-create"),
    path("<int:pk>/", TourDetailView.as_view(), name="tour-detail")
]
