from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from tours.forms import TourCreateForm, TourDeleteForm, TourEditForm
from tours.models import Tour


class TourListView(ListView):
    model = Tour
    template_name = "tours/tour_list.html"
    context_object_name = "tours"

    def get_queryset(self):
        return super().get_queryset().annotate(
            invention_count=Count("inventions")
        )

class TourCreateView(CreateView):
    model = Tour
    form_class = TourCreateForm
    template_name = "tours/tour_create.html"

    def get_success_url(self) -> str:
        if self.object is None:
            raise ValueError("The tour must be saved before redirecting.")

        return reverse(
            "tours:tour-detail",
            kwargs={"pk": self.object.pk},
        )

class TourDetailView(DetailView):
    model = Tour
    template_name = "tours/tour_detail.html"
    context_object_name = "tour"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inventions"] = (
            self.object.inventions.select_related("collection")
        )
        return context

class TourUpdateView(UpdateView):
    model = Tour
    form_class = TourEditForm
    template_name = "tours/tour_edit.html"
    context_object_name = "tour"

    def get_success_url(self) -> str:
        if self.object is None:
            raise ValueError("The tour must be saved before redirecting.")

        return reverse(
            "tours:tour-detail",
            kwargs={"pk": self.object.pk},
        )

def tour_delete(request, pk):
    tour = get_object_or_404(Tour, pk=pk)

    if request.method == "POST":
        form = TourDeleteForm(
            request.POST,
            instance=tour,
        )

        if form.is_valid():
            tour.delete()
            return redirect("tours:tour-list")
    else:
        form = TourDeleteForm(instance=tour)

    context = {
        "tour": tour,
        "form": form,
    }

    return render(
        request,
        "tours/tour_delete.html",
        context,
    )
