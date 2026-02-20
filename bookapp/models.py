from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Book(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Reading", "Reading"),
        ("Finished", "Finished"),
    ]

    title = models.CharField(max_length=50)

    # mínimo 1 página
    pages = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )

    # rating opcional entre 1 y 5
    rating = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    published_date = models.DateField()
    read_date = models.DateField(null=True, blank=True)

    authors = models.ManyToManyField(Author, blank=True)

    cover_image = models.ImageField(
        upload_to="covers/",
        null=True,
        blank=True
    )

    def clean(self):
        super().clean()

        if self.read_date and self.read_date < self.published_date:
            raise ValidationError(
                {"read_date": "The read date must be after the published date"}
            )

    def __str__(self):
        return self.title