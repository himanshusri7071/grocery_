from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate, Seller, Customer

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Seller)
admin.site.register(Customer)