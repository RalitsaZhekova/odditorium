from django import template

register = template.Library()

ABSURDITY_LABELS = {
    1: "Slightly peculiar",
    2: "Delightfully unnecessary",
    3: "Seriously questionable",
    4: "Institutionally concerning",
    5: "Utterly ridiculous"
}


@register.inclusion_tag("inventions/absurdity_badge.html")
def absurdity_badge(level):
    return {
        "level": level,
        "label": ABSURDITY_LABELS.get(level, "Not rated")
    }
