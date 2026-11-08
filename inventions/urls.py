from django.urls import path

from inventions.views import InventionCreateView, InventionDetailView, InventionListView, InventionUpdateView, invention_delete

app_name = "inventions"

urlpatterns = [
    path("", InventionListView.as_view(), name="invention-list"),
    path("create/", InventionCreateView.as_view(), name="invention-create"),
    path(
        "<int:pk>/",
        InventionDetailView.as_view(),
        name="invention-detail"
    ),
    path(
        "<int:pk>/edit/",
        InventionUpdateView.as_view(),
        name="invention-edit"
    ),
    path(
        "<int:pk>/delete/",
        invention_delete,
        name="invention-delete"
    )
]
