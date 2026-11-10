from django import forms
from common.mixins import DisabledFormMixin

from tours.models import Tour
from galleries.models import Collection


class TourBaseForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [
            "name",
            "description",
            "duration_minutes",
            "inventions"
        ]
        labels = {
            "name": "Tour name",
            "description": "About this tour",
            "duration_minutes": "Estimated duration in minutes",
            "inventions": "Featured inventions"
        }
        help_texts = {
            "name": "Choose a unique name between 3 and 100 characters.",
            "description": "Describe the experience in at least 20 characters.",
            "duration_minutes": "Allow between 5 and 180 minutes.",
            "inventions": "Choose at least one invention for this tour."
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "e.g. A Tour of Terrible Solutions"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "What connects these wonderfully useless ideas?",
                    "rows": 5
                }
            ),
            "duration_minutes": forms.NumberInput(
                attrs={"min": 5, "max": 180}
            ),
            "inventions": forms.CheckboxSelectMultiple()
        }
        error_messages = {
            "name": {
                "required": "Give your tour a name.",
                "unique": "A tour with this name already exists.",
                "min_length": "The tour name must have at least 3 characters.",
                "max_length": "Keep the tour name within 100 characters."
            },
            "description": {
                "required": "Tell visitors what this tour is about.",
                "min_length": "Describe the tour in at least 20 characters."
            },
            "duration_minutes": {
                "required": "Enter the estimated tour duration.",
                "invalid": "Enter a whole number of minutes.",
                "min_value": "A tour must last at least 5 minutes.",
                "max_value": "A tour cannot exceed 180 minutes."
            },
            "inventions": {
                "required": "Choose at least one invention.",
                "invalid_choice": "Choose from the available inventions."
            }
        }

class TourCreateForm(TourBaseForm):
    pass

class TourEditForm(TourBaseForm):
    pass

class TourDeleteForm(DisabledFormMixin, TourBaseForm):
    class Meta(TourBaseForm.Meta):
        fields = ["name"]
        help_texts = {
            "name": "Confirm that this is the tour you want to delete."
        }

class TourBuilderForm(forms.Form):
    collection = forms.ModelChoiceField(
        queryset=Collection.objects.all(),
        required=False,
        empty_label="Across the whole museum",
        label="Where should we explore?",
        error_messages={
            "invalid_choice": "Choose one of the available collections."
        },
    )
    max_absurdity = forms.IntegerField(
        min_value=1,
        max_value=5,
        initial=5,
        label="Maximum absurdity level",
        help_text="From 1 (slightly peculiar) to 5 (utterly ridiculous).",
        error_messages={
            "required": "Choose the maximum absurdity level.",
            "invalid": "Enter a whole number.",
            "min_value": "Choose a level from 1 to 5.",
            "max_value": "Choose a level from 1 to 5."
        },
    )
    exhibit_count = forms.IntegerField(
        min_value=1,
        max_value=12,
        initial=3,
        label="Number of exhibits",
        help_text="Choose between 1 and 12 inventions.",
        error_messages={
            "required": "Choose how many inventions to include.",
            "invalid": "Enter a whole number.",
            "min_value": "Include at least one invention.",
            "max_value": "Keep your tour within 12 inventions."
        }
    )

class TourPreviewSaveForm(TourBaseForm):
    def __init__(self, *args, invention_ids, **kwargs):
        super().__init__(*args, **kwargs)

        self.initial["inventions"] = invention_ids
        self.fields["inventions"].disabled = True
        self.fields["inventions"].help_text = (
            "These inventions come from your preview. "
            "Generate another preview to change the selection."
        )
