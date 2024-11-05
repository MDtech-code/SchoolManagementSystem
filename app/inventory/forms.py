from django import forms
from .models import Item, ItemsInStock, Vendor, PurchaseRecord, ReturnToVendor, Issuance, ReturnFromDepartment, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {'category':forms.Select(attrs={'class':'form-select'}),
                   'description':forms.Textarea(attrs={'class':'form-control'}),
                   'name':forms.TextInput(attrs={'class':'form-control'}),
                   'unit_price': forms.NumberInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Choose a Category"
            
    

class ItemsInStockForm(forms.ModelForm):
    class Meta:
        model = ItemsInStock
        fields = '__all__'
        widgets = {'item':forms.Select(attrs={'class':'form-select'}),
                   'quantity':forms.NumberInput(attrs={'class':'form-control'}),
                   'reorder_level':forms.NumberInput(attrs={'class':'form-control'})}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].empty_label = "Choose a Item"
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        widgets = {'address':forms.Textarea(attrs={'class':'form-control'}),
                   'contact_no': forms.NumberInput(attrs={'class':'form-control'}),
                   'name': forms.TextInput(attrs={'class':'form-control'})}

class PurchaseRecordForm(forms.ModelForm):
    class Meta:
        model = PurchaseRecord
        fields = '__all__'
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'stock_item':forms.Select(attrs={'class':'form-select'}),
            'vendor':forms.Select(attrs={'class':'form-select'}),
            'item':forms.Select(attrs={'class':'form-select'}),
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'invoice_number':forms.TextInput(attrs={'class':'form-control'}),
            'purchase_date':forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set default value for invoice_number
        self.fields['invoice_number'].initial = "NF!4#1380-7" 
        self.fields['stock_item'].empty_label = 'Choose the Stock Item'
        self.fields['vendor'].empty_label = 'Choose a Vendor'
        self.fields['item'].empty_label = 'Choose a Item'

class ReturnToVendorForm(forms.ModelForm):
    class Meta:
        model = ReturnToVendor
        fields = '__all__'
        widgets = {'return_date':forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
                   'stock_item':forms.Select(attrs={'class':'form-select'}),
                   'vendor':forms.Select(attrs={'class':'form-select'}),
                   'item':forms.Select(attrs={'class':'form-select'}),
                   'quantity': forms.NumberInput(attrs={'class':'form-control'}),
                   }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock_item'].empty_label = "Choose a Stock Item"
        self.fields['vendor'].empty_label = "Choose a Vendor"
        self.fields['item'].empty_label = "Choose a Item"

class IssuanceForm(forms.ModelForm):
    class Meta:
        model = Issuance
        fields = '__all__'
        widgets = {'issue_date':forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
                   'stock_item':forms.Select(attrs={'class':'form-select'}),
                   'department':forms.Select(attrs={'class':'form-select'}),
                   'item':forms.Select(attrs={'class':'form-select'}),
                   'quantity':forms.NumberInput(attrs={'class':'form-control'}),
                   'recipient':forms.TextInput(attrs={'class':'form-control'})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock_item'].empty_label = "Choose a Stock Item"
        self.fields['department'].empty_label = "Choose a Department"
        self.fields['item'].empty_label = "Choose a Item"

from django import forms

class ReturnFromDepartmentForm(forms.ModelForm):
    class Meta:
        model = ReturnFromDepartment
        fields = '__all__'
        widgets = {
            'department': forms.Select(attrs={'class': 'form-select'}),
            'stock_item': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Choose a department"
        self.fields['stock_item'].empty_label = "Choose a stock item"
