from django.db import models

from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models


class Tour(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    description = models.TextField(
        validators=[MinLengthValidator(20)]
    )
    duration_minutes = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(180)
        ],
    )
    inventions = models.ManyToManyField(
        "inventions.Invention",
        related_name="tours"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
