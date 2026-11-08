from django.db.models import Count
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from tours.forms import TourCreateForm
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
