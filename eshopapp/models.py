from django.db import models

# Create your models here.

from django.conf import settings


class Category(models.Model):
    """
    Category：laptop、tablet、AIO、desktop、server
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    """
    Manufacturer
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(blank=True, null=True, max_length=200, upload_to='manufacturer/uploads/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product
    """
    model = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, max_length=200, upload_to='product/uploads/%Y/%m/%d/')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    sold = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category, related_name='product_category')
    manufacturer = models.ForeignKey(Manufacturer, related_name='product_of', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model


class DeliveryAddress(models.Model):
    """
    Delivery Address
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='delivery_address_of', )
    contact_person = models.CharField(max_length=200)
    contact_mobile_phone = models.CharField(max_length=200)
    delivery_address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.delivery_address


class UserProfile(models.Model):
    """
    UserProfile
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_of', )
    mobile_phone = models.CharField(blank=True, null=True, max_length=200)
    nickname = models.CharField(blank=True, null=True, max_length=200)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(blank=True, null=True, max_length=200, upload_to='user/uploads/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delivery_address = models.ForeignKey(DeliveryAddress, related_name='user_delivery_address',
                                         on_delete=models.CASCADE, blank=True, null=True, )
