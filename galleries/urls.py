from django.urls import path

from galleries.views import CollectionListView

app_name = "galleries"

urlpatterns = [
    path("", CollectionListView.as_view(), name="collection-list")
]
