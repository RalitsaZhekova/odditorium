from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DetailView, ListView, UpdateView

from galleries.models import Collection
from galleries.forms import CollectionForm, CollectionEditForm, CollectionDeleteForm


class CollectionListView(ListView):
    model = Collection
    template_name = "galleries/collection_list.html"
    context_object_name = "collections"

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = "galleries/collection_create.html"
    success_url = reverse_lazy("galleries:collection-list")

class CollectionDetailView(DetailView):
    model = Collection
    template_name = "galleries/collection_detail.html"
    context_object_name = "collection"

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionEditForm
    template_name = "galleries/collection_edit.html"
    context_object_name = "collection"

    def get_success_url(self) -> str:
        return reverse(
            "galleries:collection-detail",
            kwargs={"pk": self.object.pk}
        )

def collection_delete(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    form = CollectionDeleteForm(instance=collection)

    if request.method == "POST":
        collection.delete()
        return redirect("galleries:collection-list")

    context = {
        "collection": collection,
        "form": form
    }

    return render(
        request,
        "galleries/collection_delete.html",
        context
    )
