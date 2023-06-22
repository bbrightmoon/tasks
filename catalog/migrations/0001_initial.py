# Generated by Django 4.2.2 on 2023-06-19 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Название категории"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "db_table": "category",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="фотография",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(default=0, null=True, verbose_name="цена"),
                ),
                (
                    "discount",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="акция"
                    ),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="количество"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="создано"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="обновлено"),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="ProductRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rate",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (5, "incredible"),
                            (4, "excellent"),
                            (3, "very good"),
                            (2, "good"),
                            (1, "bad"),
                        ]
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                    ),
                ),
            ],
        ),
    ]
