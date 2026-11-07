from django.urls import path

from galleries.views import CollectionListView, CollectionCreateView

app_name = "galleries"

urlpatterns = [
    path("", CollectionListView.as_view(), name="collection-list"),
    path("create/", CollectionCreateView.as_view(), name="collection-create")
]
