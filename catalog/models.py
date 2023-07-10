from django.db import models

from user.models import User
from catalog.utils import compress
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Название категории"
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=250,  verbose_name='название'
    )
    description = models.TextField(
        blank=True, null=True, verbose_name='описание'
    )
    image = models.ImageField(
        upload_to="images/", null=True, blank=True, verbose_name='фотография'
    )
    price = models.IntegerField(
        default=0, null=True, blank=False, verbose_name='цена'
    )
    discount = models.BooleanField(
        null=True, blank=True, default=False, verbose_name='акция'
    )
    amount = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='количество'
    )
    created = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name='создано'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='обновлено'
    )
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE,
        null=True, verbose_name='категория')
    rate = models.FloatField(
        null=True, blank=True, verbose_name='рейтинг', validators=[MinValueValidator(0)]
    )

    def __str__(self) -> str:
        return str(self.title)

    def save(self, *args, **kwargs):
        new_im = compress(self.image)
        self.image = new_im
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

