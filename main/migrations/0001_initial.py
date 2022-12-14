# Generated by Django 4.1.2 on 2022-10-07 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя покупателя')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(verbose_name='Дата заказа')),
                ('ship_date', models.DateField(verbose_name='Дата доставки')),
                ('paid_date', models.DateField(verbose_name='Дата оплаты')),
                ('status', models.CharField(max_length=100, verbose_name='Статус заказа')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer', verbose_name='Покупатель')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория товара')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='Итого')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='Номер заказа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Товар')),
            ],
        ),
    ]
