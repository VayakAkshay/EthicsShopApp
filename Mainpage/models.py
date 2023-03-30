from django.db import models
import datetime


class ProductData(models.Model):
    product_id = models.AutoField
    product_name = models.TextField(max_length=200,default="")
    product_desc = models.TextField(max_length=5000,default="")
    product_img = models.ImageField(upload_to="product_img/")
    product_gender = models.TextField(max_length=20,
                                      choices=(("Male","Male"),("Female","Female")),default="Male")
    product_category = models.TextField(max_length=100,default="")
    product_subcategory = models.TextField(max_length=100,default="")
    product_price = models.IntegerField(default=0)
    product_size = models.TextField(max_length=100,default="")

    
class CartItems(models.Model):
    cart_id = models.AutoField
    product_id = models.IntegerField(default=0)
    product_name = models.TextField(max_length=1000,default="")
    user_id = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    product_size = models.TextField(max_length=100,default="")
    full_name = models.TextField(max_length=100,default="")
    
class ContactData(models.Model):
    contact_id = models.AutoField
    contact_email = models.EmailField(max_length=200,default="")
    contact_message = models.TextField(max_length=5000,default="")

    def __str__(self):
        return self.contact_email
    
class OrderItem(models.Model):
    order_id = models.AutoField
    product_id = models.IntegerField(default=0)
    product_name = models.TextField(max_length=1000,default="")
    qty = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    Order_date = models.DateField(default=datetime.date.today)
    delivery_date = models.DateField(default=datetime.date.today)
    product_size = models.TextField(max_length=10,default="")
    full_name = models.TextField(max_length=100,default="")
    
    
class ReviewData(models.Model):
    review_id = models.AutoField
    product_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    reviewer_name = models.TextField(max_length=200,default="")
    review_desc = models.TextField(max_length=5000,default="")
    date = models.DateField(default=datetime.date.today)
    review_star = models.IntegerField(default=0)
