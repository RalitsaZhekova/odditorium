from django.shortcuts import get_object_or_404

from galleries.models import Collection
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from inventions.forms import InventionCreateForm
from inventions.models import Invention


class InventionListView(ListView):
    model = Invention
    template_name = "inventions/invention_list.html"
    context_object_name = "inventions"

    def get_queryset(self):
        return super().get_queryset().select_related("collection")

class InventionCreateView(CreateView):
    model = Invention
    form_class = InventionCreateForm
    template_name = "inventions/invention_create.html"
    success_url = reverse_lazy("inventions:invention-list")

    def get_initial(self):
        initial = super().get_initial()
        collection_id = self.request.GET.get("collection")

        if collection_id and collection_id.isdecimal():
            collection = get_object_or_404(
                Collection,
                pk=int(collection_id),
            )
            initial["collection"] = collection.pk

        return initial
