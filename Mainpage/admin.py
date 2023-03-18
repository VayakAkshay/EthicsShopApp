from django.contrib import admin
from .models import ProductData,CartItems,ContactData,OrderItem,ReviewData
# Register your models here.
admin.site.register(ProductData)
admin.site.register(CartItems)
admin.site.register(ContactData)
admin.site.register(OrderItem)
admin.site.register(ReviewData)