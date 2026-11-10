from random import sample

from django.core.exceptions import ValidationError

from inventions.models import Invention


def select_tour_inventions(
    *,
    collection,
    max_absurdity,
    exhibit_count
):
    inventions = Invention.objects.select_related("collection").filter(
        absurdity_level__lte=max_absurdity
    )

    if collection is not None:
        inventions = inventions.filter(collection=collection)

    available_inventions = list(inventions)

    if len(available_inventions) < exhibit_count:
        raise ValidationError(
            f"Only {len(available_inventions)} inventions match your choices. "
            "Request fewer exhibits or broaden your selection.",
            code="insufficient_inventions"
        )

    return sample(available_inventions, exhibit_count)
