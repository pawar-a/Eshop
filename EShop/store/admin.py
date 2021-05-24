from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdmimProduct(admin.ModelAdmin):
    list_display = ["name","price","category","desc"]

# Register your models here.
admin.site.register(Product,AdmimProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
