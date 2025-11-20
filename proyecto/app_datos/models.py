from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Categories(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class PaymentMethods(models.Model):
    id_paymentmethod = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class ShippingTypes(models.Model):
    id_shippingtype = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Promotions(models.Model):
    id_promotion = models.AutoField(primary_key=True)
    promocode = models.CharField(max_length=64, default="", blank=True)
    description = models.TextField(max_length=1024, default="", blank=True)

    def __str__(self):
        return (
            f"{self.promocode} - {self.description}"
            if self.promocode
            else f"Promotion {self.id_promotion}"
        )


class Locations(models.Model):
    id_location = models.AutoField(primary_key=True)
    state = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.state


class Sizes(models.Model):
    id_size = models.AutoField(primary_key=True)
    size_label = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.size_label


class Colors(models.Model):
    id_color = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Seasons(models.Model):
    id_season = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Customers(models.Model):
    id_customer = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customers")
    age = models.IntegerField()
    gender = models.CharField(max_length=16)
    id_location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    sub_status = models.BooleanField(default=False)
    id_paymentmethod = models.ForeignKey(PaymentMethods, on_delete=models.CASCADE)
    freq_purchase = models.CharField(max_length=32)
    prev_purchases = models.IntegerField()

    def __str__(self):
        # Use readable formatting; related FK objects' __str__ will be used automatically
        return (
            f"Customer {self.id_customer}: age={self.age}, gender={self.gender}, "
            f"location={self.id_location}, subscribed={self.sub_status}, "
            f"preferred_payment={self.id_paymentmethod}, frequency={self.freq_purchase}, "
            f"previous_purchases={self.prev_purchases}"
        )


class Products(models.Model):
    id_product = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=128)
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    id_size = models.ForeignKey(Sizes, on_delete=models.SET_NULL, null=True, blank=True)
    id_color = models.ForeignKey(
        Colors, on_delete=models.SET_NULL, null=True, blank=True
    )
    id_season = models.ForeignKey(
        Seasons, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        unique_together = ["user", "name"]

    def __str__(self):
        return f"{self.name} (id={self.id_product})"


class Transactions(models.Model):
    id_transaction = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    id_customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    purchase_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField(null=True, blank=True, default=None)
    review_rate = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True, default=None
    )
    id_paymentmethod = models.ForeignKey(PaymentMethods, on_delete=models.CASCADE)
    id_shipping = models.ForeignKey(ShippingTypes, on_delete=models.CASCADE)
    dsct_applied = models.BooleanField(default=False)
    promo_used = models.BooleanField(default=False)
    id_promotion = models.ForeignKey(
        Promotions, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return (
            f"Transaction {self.id_transaction}: customer={self.id_customer}, "
            f"product={self.id_product}, amount={self.purchase_amount}"
        )
