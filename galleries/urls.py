from django.urls import path

from galleries.views import CollectionListView, CollectionCreateView, CollectionDetailView, CollectionUpdateView, collection_delete

app_name = "galleries"

urlpatterns = [
    path("", CollectionListView.as_view(), name="collection-list"),
    path("create/", CollectionCreateView.as_view(), name="collection-create"),
    path(
        "<int:pk>/",
        CollectionDetailView.as_view(),
        name="collection-detail"
    ),
    path(
        "<int:pk>/edit/",
        CollectionUpdateView.as_view(),
        name="collection-edit"
    ),
    path(
        "<int:pk>/delete/",
        collection_delete,
        name="collection-delete"
    ),
]
