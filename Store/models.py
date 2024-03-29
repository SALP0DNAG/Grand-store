from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.category}"


class SpecialProducts(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='special_products_images')

    def __str__(self):
        return f"SPECIAL {self.category}"


class Characteristics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    guarantee = models.PositiveIntegerField(default=None, verbose_name="Гарантия")
    thread_diameter = models.DecimalField(default=None, max_digits=5, decimal_places=2, verbose_name="Диаметр резьбы")
    material = models.CharField(max_length=30, default=None, verbose_name="Материал")
    mounting_method = models.CharField(max_length=30, default=None, verbose_name="Способ монтажа")
    purpose_mixer = models.CharField(max_length=50, default=None, verbose_name="Назначение смесителя")
    mixer_type = models.CharField(max_length=50, default=None, verbose_name="Тип смесителя")
    type_liner = models.CharField(max_length=50, default=None, verbose_name="Тип подводки")
    width = models.PositiveIntegerField(default=None, verbose_name="Ширина")
    length = models.PositiveIntegerField(default=None, verbose_name="Длина")
    weight = models.PositiveIntegerField(default=None, verbose_name="Вес")
    height = models.PositiveIntegerField(default=None, verbose_name="Высота")
    wear_resistance = models.CharField(max_length=20, default=None, verbose_name="Износостойкость")
    country = models.CharField(max_length=20, default=None, verbose_name="Страна производитель")
    basis = models.CharField(max_length=20, default=None, verbose_name="Основа")
    color = models.CharField(max_length=20, default=None, verbose_name="Цвет")
    putty_type = models.CharField(max_length=20, default=None, verbose_name="Тип шпатлёвки")
    drying_time = models.PositiveIntegerField(default=None, verbose_name="Время высыхания")
    volume = models.PositiveIntegerField(default=None, verbose_name="Объём")
    thickness = models.PositiveIntegerField(default=None, verbose_name="Толщина")
    glass_package = models.CharField(max_length=30, default=None, verbose_name="Стеклопакет")

    def __str__(self):
        return f"Характеристики для товара {self.product.name}"
