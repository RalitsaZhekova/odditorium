from django.db import models

from django.core.validators import MinLengthValidator
from django.db import models


class Collection(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    description = models.TextField(
        validators=[MinLengthValidator(20)]
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
