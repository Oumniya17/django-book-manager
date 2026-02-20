from django import forms
from django.core.exceptions import ValidationError
from .models import Book


class BookForm(forms.ModelForm):

    # Sobrescribimos title para controlar mensajes personalizados
    title = forms.CharField(
        max_length=50,
        required=True,
        error_messages={
            "required": "The title is mandatory",
            "max_length": "The title must be less than 50 characters long",
        }
    )

    class Meta:
        model = Book
        fields = [
            "title",
            "pages",
            "rating",
            "status",
            "published_date",
            "read_date",
            "authors",
            "cover_image",
        ]

    # Validación de fechas en el formulario
    def clean(self):
        cleaned_data = super().clean()

        published = cleaned_data.get("published_date")
        read = cleaned_data.get("read_date")

        if read and published and read < published:
            raise ValidationError(
                {"read_date": "The read date must be after the published date"}
            )

        return cleaned_data