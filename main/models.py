from django.db import models

class Customer(models.Model):
    name = models.CharField('Имя покупателя', max_length=50)
    phone = models.CharField('Телефон', max_length=11)
    email = models.EmailField('Email', max_length=100)
    city = models.CharField('Город', max_length=50)
    address = models.CharField('Адрес', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

class Category(models.Model):
    name = models.CharField('Название категории', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    order_date = models.DateField('Дата заказа')
    ship_date = models.DateField('Дата доставки')
    paid_date = models.DateField('Дата оплаты')
    status = models.CharField('Статус заказа', max_length=100)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Product(models.Model):
    product_name = models.CharField('Название', max_length=250)
    price = models.IntegerField('Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    image = models.ImageField('Фото')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Receipt(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    total = models.IntegerField('Итого')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
