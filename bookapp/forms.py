from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    # Sobrescribimos el campo title para controlar mensajes
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
        fields = "__all__"

    # validación de fechas en el formulario (para que aparezca en form.errors)
    def clean(self):
        cleaned_data = super().clean()

        published = cleaned_data.get("published_date")
        read = cleaned_data.get("read_date")

        if read and published and read < published:
            self.add_error(
                "read_date",
                "The read date must be after the published date"
            )

        return cleaned_data
