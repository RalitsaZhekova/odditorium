from django.shortcuts import get_object_or_404, redirect, render

from galleries.models import Collection
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from inventions.forms import InventionCreateForm, InventionEditForm, InventionDeleteForm,  InventionSearchForm
from inventions.models import Invention
from django.db.models import Q
from django.db.models.functions import Lower


class InventionListView(ListView):
    model = Invention
    template_name = "inventions/invention_list.html"
    context_object_name = "inventions"

    def get_queryset(self):
        inventions = super().get_queryset().select_related("collection")
        self.search_form = InventionSearchForm(self.request.GET)

        if not self.search_form.is_valid():
            return inventions.none()

        query = self.search_form.cleaned_data["query"]
        collection = self.search_form.cleaned_data["collection"]
        ordering = self.search_form.cleaned_data["ordering"] or "name"

        if query:
            inventions = inventions.filter(
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(inventor__icontains=query)
            )

        if collection is not None:
            inventions = inventions.filter(collection=collection)

        inventions = inventions.annotate(
            name_sort=Lower("name")
        )

        ordering = {
            "name": "name_sort",
            "-name": "-name_sort",
        }.get(ordering, ordering)

        return inventions.order_by(ordering, "name_sort", "pk")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.search_form
        return context

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

class InventionDetailView(DetailView):
    model = Invention
    template_name = "inventions/invention_detail.html"
    context_object_name = "invention"

    def get_queryset(self):
        return super().get_queryset().select_related("collection")


class InventionUpdateView(UpdateView):
    model = Invention
    form_class = InventionEditForm
    template_name = "inventions/invention_edit.html"
    context_object_name = "invention"

    def get_success_url(self) -> str:
        return reverse(
            "inventions:invention-detail",
            kwargs={"pk": self.object.pk},
        )


def invention_delete(request, pk):
    invention = get_object_or_404(Invention, pk=pk)

    if request.method == "POST":
        form = InventionDeleteForm(
            request.POST,
            instance=invention,
        )

        if form.is_valid():
            invention.delete()
            return redirect("inventions:invention-list")
    else:
        form = InventionDeleteForm(instance=invention)

    context = {
        "invention": invention,
        "form": form,
    }

    return render(
        request,
        "inventions/invention_delete.html",
        context,
    )
