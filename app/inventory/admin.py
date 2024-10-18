'''
from django.contrib import admin
from .models import (
    Category, Vendor, Item, ItemsInStock, ReturnToVendor,
    PurchaseRecord, Department, Issuance, ReturnFromDepartment
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact_no', 'address']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'unit_price']

@admin.register(ItemsInStock)
class ItemsInStockAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'quantity', 'reorder_level']

@admin.register(ReturnToVendor)
class ReturnToVendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'stock_item', 'vendor', 'quantity', 'return_date']

@admin.register(PurchaseRecord)
class PurchaseRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'stock_item', 'vendor', 'amount', 'invoice_number', 'purchase_date', 'quantity']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Issuance)
class IssuanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'stock_item', 'issue_date', 'quantity', 'recipient']

@admin.register(ReturnFromDepartment)
class ReturnFromDepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'stock_item', 'quantity', 'return_date']
'''