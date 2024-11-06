
# from django.contrib import admin
# from .models import Item, ItemsInStock, Vendor, PurchaseRecord, ReturnToVendor, Issuance, ReturnFromDepartment

# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'unit_price')
#     search_fields = ('name', 'category__name')
#     list_filter = ('category',)
#     ordering = ('name',)

# @admin.register(ItemsInStock)
# class ItemsInStockAdmin(admin.ModelAdmin):
#     list_display = ('item', 'quantity', 'reorder_level')
#     search_fields = ('item__name',)
#     list_filter = ('quantity',)
#     ordering = ('item',)

# @admin.register(Vendor)
# class VendorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'contact_no', 'address')
#     search_fields = ('name', 'contact_no')
#     ordering = ('name',)

# @admin.register(PurchaseRecord)
# class PurchaseRecordAdmin(admin.ModelAdmin):
#     list_display = ('stock_item', 'vendor', 'amount', 'purchase_date', 'quantity')
#     search_fields = ('stock_item__item__name', 'vendor__name', 'invoice_number')
#     list_filter = ('purchase_date', 'vendor')
#     date_hierarchy = 'purchase_date'
#     ordering = ('-purchase_date',)

# @admin.register(ReturnToVendor)
# class ReturnToVendorAdmin(admin.ModelAdmin):
#     list_display = ('stock_item', 'vendor', 'quantity', 'return_date')
#     search_fields = ('stock_item__item__name', 'vendor__name')
#     list_filter = ('return_date', 'vendor')
#     date_hierarchy = 'return_date'
#     ordering = ('-return_date',)

# @admin.register(Issuance)
# class IssuanceAdmin(admin.ModelAdmin):
#     list_display = ('department', 'stock_item', 'issue_date', 'quantity', 'recipient')
#     search_fields = ('department__name', 'stock_item__item__name', 'recipient')
#     list_filter = ('issue_date', 'department')
#     date_hierarchy = 'issue_date'
#     ordering = ('-issue_date',)

# @admin.register(ReturnFromDepartment)
# class ReturnFromDepartmentAdmin(admin.ModelAdmin):
#     list_display = ('department', 'stock_item', 'quantity', 'return_date')
#     search_fields = ('department__name', 'stock_item__item__name')
#     list_filter = ('return_date', 'department')
#     date_hierarchy = 'return_date'
#     ordering = ('-return_date',)
