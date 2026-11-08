from django.db import models

from inventions.validators import validate_image_size
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator


class Invention(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    description = models.TextField(
        validators=[MinLengthValidator(20)]
    )
    image = models.ImageField(
        upload_to="inventions/",
        blank=True,
        validators=[validate_image_size]
    )
    inventor = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(3)]
    )
    absurdity_level = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    collection = models.ForeignKey(
        "galleries.Collection",
        on_delete=models.PROTECT,
        related_name="inventions"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
