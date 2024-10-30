from django.db import models
from app.common.models import TimeStampedModel,Category
from app.academic.models import Department

class Item(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    # sku = models.CharField(max_length=100, unique=True)  # Unique Stock Keeping Unit
    # is_active = models.BooleanField(default=True)  # To indicate if item is active

    def __str__(self):
        return f"{self.name} - {self.category.name}"
    
class ItemsInStock(TimeStampedModel):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()
    # location = models.CharField(max_length=255)  # Storage location

    def __str__(self):
        return f"{self.item.name} (Stock: {self.quantity})"

class Vendor(TimeStampedModel):
    address = models.TextField()
    contact_no = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    # email = models.EmailField(null=True, blank=True)  # Optional email field

    def __str__(self):
        return f"{self.name} ({self.contact_no})"
    
class PurchaseRecord(TimeStampedModel):
    stock_item = models.ForeignKey(ItemsInStock, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_number = models.CharField(max_length=255)
    purchase_date = models.DateField()
    quantity = models.PositiveIntegerField()
    # total_cost = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Calculated field

    # Change to nullable
    
    def __str__(self):
        return f"Purchase of {self.quantity} {self.stock_item.item.name} from {self.vendor.name} for {self.amount} on {self.purchase_date}"
    
class ReturnToVendor(TimeStampedModel):
    stock_item = models.ForeignKey(ItemsInStock, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    return_date = models.DateField()
    # reason = models.TextField(null=True, blank=True)  # Reason for return

    # Change to nullable

    def __str__(self):
        return f"Return {self.quantity} of {self.stock_item.item.name} to {self.vendor.name}"

class Issuance(TimeStampedModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    stock_item = models.ForeignKey(ItemsInStock, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    issue_date = models.DateField()
    quantity = models.PositiveIntegerField()
    recipient = models.CharField(max_length=255)
    # notes = models.TextField(null=True, blank=True)  # Optional notes for issuance

    # Add ForeignKey to Item

    def __str__(self):
        return f"Issued {self.quantity} of {self.stock_item.item.name} to {self.recipient} from {self.department.name}"


class ReturnFromDepartment(TimeStampedModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    stock_item = models.ForeignKey(ItemsInStock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    return_date = models.DateField()
    condition = models.CharField(max_length=255, null=True, blank=True)  # Condition of returned item

    def __str__(self):
        return f"{self.quantity} of {self.stock_item.item.name} returned from {self.department.name} on {self.return_date}"
