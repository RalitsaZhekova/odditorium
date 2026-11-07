from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from galleries.models import Collection
from galleries.forms import CollectionForm


class CollectionListView(ListView):
    model = Collection
    template_name = "galleries/collection_list.html"
    context_object_name = "collections"

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = "galleries/collection_create.html"
    success_url = reverse_lazy("galleries:collection-list")
