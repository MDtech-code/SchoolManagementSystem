from django import forms
from .models import Item, ItemsInStock, Vendor, PurchaseRecord, ReturnToVendor, Issuance, ReturnFromDepartment, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {'category':forms.Select(attrs={'class':'form-control'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        first_item = Item.objects.first()
        if first_item:
            self.fields['category'].initial = first_item
            
    

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
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set default value for invoice_number
        self.fields['invoice_number'].initial = "NF!4#1380-7"  # Replace with your desired value

        # Set the first item of stock_item as default
        first_stock_item = ItemsInStock.objects.first()  # Get the first stock item
        if first_stock_item:
            self.fields['stock_item'].initial = first_stock_item


class ReturnToVendorForm(forms.ModelForm):
    class Meta:
        model = ReturnToVendor
        fields = '__all__'
        widgets = {'return_date':forms.DateInput(attrs={'type':'date'})}

class IssuanceForm(forms.ModelForm):
    class Meta:
        model = Issuance
        fields = '__all__'
        widgets = {'issue_date':forms.DateInput(attrs={'type':'date'})}

class ReturnFromDepartmentForm(forms.ModelForm):
    class Meta:
        model = ReturnFromDepartment
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']



