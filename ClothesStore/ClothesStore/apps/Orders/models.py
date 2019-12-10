from django.db import models
from Users.models import SimpleUser
from Products.models import Product
from django.db.models.signals import post_save
# Create your models here.

class Status(models.Model):
    name= models.CharField(max_length=20, blank=True, null=True, default=None)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(SimpleUser, blank=True, null=True, default=None, on_delete=models.CASCADE)
    status=models.ForeignKey(Status, on_delete=models.CASCADE)
    customer_addres = models.CharField(max_length=50)
    total_price=models.DecimalField(max_digits=10, decimal_places=2, default=0) #total_product_price +
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "Заказ %s" % self.id

    def save(self, *args, **kwargs):
        super(Order,self).save(*args, **kwargs)

class ProductinOrder(models.Model):
    product=models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price=models.DecimalField(max_digits=10, decimal_places=2,default=0)#price*Quantity
    def __str__(self):
        return "product total %s :" % self.total_price


    def save(self, *args, **kwargs):
        price_per_item = self.product.product_price
        self.price_per_item = price_per_item
        self.total_price=self.quantity * self.price_per_item

        super(ProductinOrder,self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
    order=instance.order
    all_products_in_order = ProductinOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price+=item.total_price

    instance.order.total_price=order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductinOrder)
