from django import forms

from inventions.models import Invention
from galleries.models import Collection

from common.mixins import DisabledFormMixin


class InventionBaseForm(forms.ModelForm):
    class Meta:
        model = Invention
        fields = [
            "name",
            "description",
            "image",
            "inventor",
            "absurdity_level",
            "collection"
        ]
        labels = {
            "name": "Invention name",
            "description": "About this invention",
            "image": "Invention image",
            "inventor": "Inventor",
            "absurdity_level": "Absurdity level",
            "collection": "Museum collection"
        }
        help_texts = {
            "description": "Explain its questionable purpose in at least 20 characters.",
            "image": "Optional. Upload an image up to 5 MB.",
            "absurdity_level": "Choose from 1 (slightly peculiar) to 5 (utterly ridiculous).",
            "collection": "Choose the collection where this invention belongs."
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "e.g. The Automatic Apology Machine"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "What does it do, and why would anyone need it?",
                    "rows": 5
                }
            ),
            "inventor": forms.TextInput(
                attrs={"placeholder": "e.g. Professor Reginald Oops"}
            ),
            "absurdity_level": forms.NumberInput(
                attrs={"min": 1, "max": 5}
            ),
        }
        error_messages = {
            "name": {
                "required": "Give your invention a name.",
                "unique": "An invention with this name already exists.",
                "min_length": "The invention name must have at least 3 characters.",
                "max_length": "Keep the invention name within 100 characters."
            },
            "description": {
                "required": "Explain what this invention does.",
                "min_length": "Describe the invention in at least 20 characters."
            },
            "image": {
                "invalid_image": (
                    "Upload a valid image file, such as a JPEG or PNG."
                )
            },
            "inventor": {
                "required": "Tell us who invented it.",
                "min_length": "The inventor's name must have at least 3 characters.",
                "max_length": "Keep the inventor's name within 80 characters."
            },
            "absurdity_level": {
                "required": "Choose an absurdity level.",
                "invalid": "Enter a whole number.",
                "min_value": "The absurdity level must be at least 1.",
                "max_value": "The absurdity level cannot exceed 5."
            },
            "collection": {
                "required": "Choose a collection for this invention.",
                "invalid_choice": "Choose one of the available collections."
            }
        }


class InventionCreateForm(InventionBaseForm):
    pass

class InventionEditForm(InventionBaseForm):
    pass

class InventionDeleteForm(DisabledFormMixin, InventionBaseForm):
    class Meta(InventionBaseForm.Meta):
        fields = ["name"]
        help_texts = {
            "name": "Confirm that this is the invention you want to delete.",
        }

class InventionSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        max_length=100,
        label="Search inventions",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name, description, or inventor"}
        ),
        error_messages={
            "max_length": "Keep your search within 100 characters."
        }
    )
    collection = forms.ModelChoiceField(
        queryset=Collection.objects.all(),
        required=False,
        empty_label="All collections",
        label="Collection",
        error_messages={
            "invalid_choice": "Choose one of the available collections."
        },
    )
    ordering = forms.ChoiceField(
        required=False,
        label="Sort by",
        choices=[
            ("name", "Name: A–Z"),
            ("-name", "Name: Z–A"),
            ("-created_at", "Newest first"),
            ("-absurdity_level", "Most absurd first"),
            ("absurdity_level", "Least absurd first")
        ],
        error_messages={
            "invalid_choice": "Choose one of the available sorting options."
        },
    )
