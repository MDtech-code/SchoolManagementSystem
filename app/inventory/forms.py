from django import forms
from .models import Item, ItemsInStock, Vendor, PurchaseRecord, ReturnToVendor, Issuance, ReturnFromDepartment, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
    

class ItemsInStockForm(forms.ModelForm):
    class Meta:
        model = ItemsInStock
        fields = '__all__'

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseRecordForm(forms.ModelForm):
    class Meta:
        model = PurchaseRecord
        fields = '__all__'

class ReturnToVendorForm(forms.ModelForm):
    class Meta:
        model = ReturnToVendor
        fields = '__all__'

class IssuanceForm(forms.ModelForm):
    class Meta:
        model = Issuance
        fields = '__all__'

class ReturnFromDepartmentForm(forms.ModelForm):
    class Meta:
        model = ReturnFromDepartment
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']



