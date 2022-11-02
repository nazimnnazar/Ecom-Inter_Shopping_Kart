from django.db import models
from core.models import*
# Create your models here.

#cart

class CartList(models.Model):
    cart_id = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItems(models.Model):
    prod = models.ForeignKey(products, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList, on_delete=models.CASCADE)
    quan = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

    def total(self):
        return self.prod.price * self.quan