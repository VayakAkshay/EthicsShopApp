from django.contrib import admin
from .models import ProductData,CartItems,ContactData,OrderItem,ReviewData

class ProductDataAdmin(admin.ModelAdmin):
    list_display = ["product_name","product_gender","product_category","product_subcategory","product_price"]

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ["user_id","full_name","product_id","qty"]

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ["user_id","full_name","product_id","qty","Order_date","delivery_date","product_size"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user_id","reviewer_name","date","product_id","review_star"]

admin.site.register(ProductData,ProductDataAdmin)
admin.site.register(CartItems,CartItemsAdmin)
admin.site.register(ContactData)
admin.site.register(OrderItem,OrderItemsAdmin)
admin.site.register(ReviewData,ReviewAdmin)