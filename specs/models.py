from django.db import models
from django.conf import settings
from .utils import send_email_with_attachment


class Industry(models.Model):
    industry = models.CharField(max_length=100, default='')
    product_type = models.CharField(max_length=100, default='')


class Products(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.PROTECT)
    model = models.CharField(max_length=100, default='')
    CHOICES = (
        ('L', 'L'), ('S', 'S'), ('M', 'M'), ('XL', 'XL'), ('XXL', 'XXL')
    )
    size = models.CharField(choices=CHOICES, max_length=100)
    price = models.IntegerField(default=10)

    def __str__(self):
        return str(self.industry.industry) + '| model: ' + str(self.model) + '| size: ' + str(self.size) + '| price: ' + str(self.price)


class OrderDetails(models.Model):
    customer_name = models.CharField(default='', max_length=100)
    deliver_address = models.CharField(default='', max_length=1000)
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    industry = models.ForeignKey(Industry, on_delete=models.PROTECT, null=True)


class Invoice(models.Model):
    customer_name = models.CharField(max_length=100, default='')


class PurchaseProduct(models.Model):
    customer_name = models.CharField(default='', max_length=100)
    shipping_address = models.CharField(default='', max_length=100)
    pincode = models.IntegerField(default=0)
    city = models.CharField(default='', max_length=100)
    state = models.CharField(default='', max_length=100)
    carts = models.ManyToManyField(Products)
    email = models.EmailField(default='', max_length=100)

    def __str__(self):
        return self.customer_name

    def save(self, *args, **kwargs):
        email_from = settings.EMAIL_HOST_USER
        send_email_with_attachment(email_from, self.email, self.shipping_address, self.carts.all(), self.city, self.state, self.pincode)
        super(PurchaseProduct, self).save(*args, **kwargs)


class ComplaintForm(models.Model):
    email = models.CharField(max_length=1000, default='abc@gmail.com')
    customer_name = models.CharField(default='', max_length=100)
    file = models.FileField(upload_to='attachments/', null=True)
    delivery_address = models.CharField(default='', max_length=1000)


class PlacedOrder(models.Model):
    shipping_address = models.CharField(default='', max_length= 100)
    order_list = models.ManyToManyField(Products)
    invoice_no = models.IntegerField()
    sending_address = models.CharField(default='', max_length=100)
