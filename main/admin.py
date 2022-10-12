from django.contrib import admin
from .models import Customer
from .models import Category
from .models import Order
from .models import Product
from .models import Receipt

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Receipt)

