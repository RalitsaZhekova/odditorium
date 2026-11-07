from django.shortcuts import render

from django.views.generic import ListView

from galleries.models import Collection


class CollectionListView(ListView):
    model = Collection
    template_name = "galleries/collection_list.html"
    context_object_name = "collections"
