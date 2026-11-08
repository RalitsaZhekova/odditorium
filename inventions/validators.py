from django.core.exceptions import ValidationError


def validate_image_size(value):
    max_size = 5 * 1024 * 1024

    if value.size > max_size:
        raise ValidationError(
            "Choose an image smaller than 5 MB.",
            code="image_too_large"
        )
