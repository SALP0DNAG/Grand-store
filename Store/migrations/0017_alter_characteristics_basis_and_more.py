# Generated by Django 5.0.1 on 2024-07-14 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0016_alter_characteristics_basis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='basis',
            field=models.CharField(blank=True, max_length=20, verbose_name='Основа'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='color',
            field=models.CharField(blank=True, max_length=20, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='country',
            field=models.CharField(blank=True, max_length=20, verbose_name='Страна производитель'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='drying_time',
            field=models.PositiveIntegerField(blank=True, verbose_name='Время высыхания'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='glass_package',
            field=models.CharField(blank=True, max_length=30, verbose_name='Стеклопакет'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='guarantee',
            field=models.PositiveIntegerField(blank=True, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='height',
            field=models.PositiveIntegerField(blank=True, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='length',
            field=models.PositiveIntegerField(blank=True, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='material',
            field=models.CharField(blank=True, max_length=30, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='mixer_type',
            field=models.CharField(blank=True, max_length=50, verbose_name='Тип смесителя'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='mounting_method',
            field=models.CharField(blank=True, max_length=30, verbose_name='Способ монтажа'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='Store.product'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='purpose_mixer',
            field=models.CharField(blank=True, max_length=50, verbose_name='Назначение смесителя'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='putty_type',
            field=models.CharField(blank=True, max_length=20, verbose_name='Тип шпатлёвки'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='thickness',
            field=models.PositiveIntegerField(blank=True, verbose_name='Толщина'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='thread_diameter',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Диаметр резьбы'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='type_liner',
            field=models.CharField(blank=True, max_length=50, verbose_name='Тип подводки'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='volume',
            field=models.PositiveIntegerField(blank=True, verbose_name='Объём'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='wear_resistance',
            field=models.CharField(blank=True, max_length=20, verbose_name='Износостойкость'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='weight',
            field=models.PositiveIntegerField(blank=True, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='width',
            field=models.PositiveIntegerField(blank=True, verbose_name='Ширина'),
        ),
    ]
