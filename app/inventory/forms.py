from django import forms
from .models import Item, ItemsInStock, Vendor, PurchaseRecord, ReturnToVendor, Issuance

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'description', 'name', 'unit_price']

class ItemsInStockForm(forms.ModelForm):
    class Meta:
        model = ItemsInStock
        fields = ['item', 'quantity', 'reorder_level']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'address', 'contact_no']

class PurchaseRecordForm(forms.ModelForm):
    class Meta:
        model = PurchaseRecord
        fields = ['stock_item', 'vendor', 'amount', 'invoice_number', 'purchase_date', 'quantity', 'item']

class ReturnToVendorForm(forms.ModelForm):
    class Meta:
        model = ReturnToVendor
        fields = ['stock_item', 'vendor', 'quantity', 'return_date', 'item']

class IssuanceForm(forms.ModelForm):
    class Meta:
        model = Issuance
        fields = ['department', 'stock_item', 'issue_date', 'quantity', 'recipient', 'item']
