from django.urls import path

from inventions.views import InventionCreateView, InventionListView

app_name = "inventions"

urlpatterns = [
    path("", InventionListView.as_view(), name="invention-list"),
    path("create/", InventionCreateView.as_view(), name="invention-create")
]
