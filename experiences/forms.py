from django import forms

from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            "name",
            "email",
            "company",
            "timeline",
            "message",
            "referrer",
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Your name",
            "email": "name@studio.com",
            "company": "Company / team",
            "timeline": "Timeline or event date",
            "message": "Tell us about the experience you have in mind",
            "referrer": "How did you hear about us?",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "placeholder": placeholders.get(field_name, ""),
                }
            )
            field.label = " ".join(part.capitalize() for part in field_name.split("_"))
