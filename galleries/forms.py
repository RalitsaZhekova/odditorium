from django import forms

from galleries.models import Collection


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ["name", "description"]
        labels = {
            "name": "Collection name",
            "description": "About this collection"
        }
        help_texts = {
            "name": "Choose a unique name between 3 and 80 characters.",
            "description": "Describe the collection in at least 20 characters."
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Domestic Disasters",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "What peculiar inventions belong here?",
                    "rows": 5,
                }
            )
        }
        error_messages = {
            "name": {
                "required": "Give your collection a name.",
                "unique": "A collection with this name already exists.",
                "min_length": "The collection name must have at least 3 characters.",
                "max_length": "Keep the collection name within 80 characters.",
            },
            "description": {
                "required": "Tell visitors what this collection is about.",
                "min_length": "Describe the collection in at least 20 characters.",
            }
        }
