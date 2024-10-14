from django.db import models
'''
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ItemsInStock(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item.name} - Stock: {self.quantity}"

class PurchaseRecord(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} - Purchase Record"

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name
'''