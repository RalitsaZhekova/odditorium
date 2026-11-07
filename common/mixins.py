from django.forms import Field


class DisabledFormMixin:
    fields: dict[str, Field]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True
