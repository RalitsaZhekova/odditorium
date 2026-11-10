from django.views.generic import TemplateView

from galleries.models import Collection
from inventions.models import Invention
from tours.models import Tour


class HomeView(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["collection_count"] = Collection.objects.count()
        context["invention_count"] = Invention.objects.count()
        context["tour_count"] = Tour.objects.count()
        context["latest_invention"] = (
            Invention.objects.select_related("collection")
            .order_by("-created_at", "-pk")
            .first()
        )

        return context
