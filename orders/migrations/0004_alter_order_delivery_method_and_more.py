# Generated by Django 5.0.1 on 2024-07-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('courier', 'Курьер (Доставка курьером)'), ('pickup', 'Самовывоз (На пункте выдачи)')], default='pickup', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Наличными'), ('card', 'Картой')], default='cash', max_length=20),
        ),
    ]
