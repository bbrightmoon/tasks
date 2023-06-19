from django.db import models


class CSVSource(models.Model):
    brand = models.CharField(
        max_length=200, null=True, blank=True
    )
    manufacturer = models.CharField(
        max_length=200, null=True, blank=True
    )
    name = models.CharField(
        max_length=250, null=True, blank=True
    )
    reviews = models.URLField(
        null=True, blank=True
    )
    text_reviews = models.TextField(
        null=True, blank=True
    )
    review_title = models.CharField(
        max_length=250, blank=True, null=True
    )
    reviews_username = models.CharField(
        max_length=200, blank=True, null=True
    )
    weight = models.CharField(
        max_length=200, null=True, blank=True
    )

    def __str__(self) -> str:
        return str(self.brand)
