from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Item, ItemsInStock, Vendor, PurchaseRecord, ReturnToVendor, Issuance
from .forms import ItemForm, VendorForm, IssuanceForm, PurchaseRecordForm, ReturnToVendorForm, ItemsInStockForm

# Item Views
class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item-list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item-list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item-list')

# ItemsInStock Views
class ItemsInStockListView(ListView):
    model = ItemsInStock
    template_name = 'items_in_stock_list.html'
    context_object_name = 'items_in_stock'

class ItemsInStockDetailView(DetailView):
    model = ItemsInStock
    template_name = 'items_in_stock_detail.html'
    context_object_name = 'stock_item'

class ItemsInStockCreateView(CreateView):
    model = ItemsInStock
    form_class = ItemsInStockForm
    template_name = 'items_in_stock_form.html'
    success_url = reverse_lazy('items-in-stock-list')

class ItemsInStockUpdateView(UpdateView):
    model = ItemsInStock
    form_class = ItemsInStockForm
    template_name = 'items_in_stock_form.html'
    success_url = reverse_lazy('items-in-stock-list')

class ItemsInStockDeleteView(DeleteView):
    model = ItemsInStock
    template_name = 'items_in_stock_confirm_delete.html'
    success_url = reverse_lazy('items-in-stock-list')

# Vendor Views
class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor_list.html'
    context_object_name = 'vendors'

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'vendor_detail.html'
    context_object_name = 'vendor'

class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'vendor_form.html'
    success_url = reverse_lazy('vendor-list')

class VendorUpdateView(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'vendor_form.html'
    success_url = reverse_lazy('vendor-list')

class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'vendor_confirm_delete.html'
    success_url = reverse_lazy('vendor-list')

# PurchaseRecord Views
class PurchaseRecordCreateView(CreateView):
    model = PurchaseRecord
    form_class = PurchaseRecordForm
    template_name = 'purchase_record_form.html'
    success_url = reverse_lazy('purchase-record-list')

# ReturnToVendor Views
class ReturnToVendorCreateView(CreateView):
    model = ReturnToVendor
    form_class = ReturnToVendorForm
    template_name = 'return_to_vendor_form.html'
    success_url = reverse_lazy('return-to-vendor-list')

# Issuance Views
class IssuanceCreateView(CreateView):
    model = Issuance
    form_class = IssuanceForm
    template_name = 'issuance_form.html'
    success_url = reverse_lazy('issuance-list')
