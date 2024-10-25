from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Item, ItemsInStock, Category
from .forms import ItemForm,ItemsInStockForm, Vendor, VendorForm, PurchaseRecord, PurchaseRecordForm, ReturnToVendor, ReturnToVendorForm, Issuance, IssuanceForm, ReturnFromDepartment, ReturnFromDepartmentForm, CategoryForm
# Item Views
class ItemListView(ListView):
    model = Item
    template_name = 'inventory/item_list.html'
    context_object_name = 'items'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'inventory/item_detail.html'
    context_object_name = 'item'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('item-list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('item-list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'inventory/item_confirm_delete.html'
    success_url = reverse_lazy('item-list')





# ItemsInStock Views
class ItemsInStockListView(ListView):
    model = ItemsInStock
    template_name = 'inventory/items_in_stock_list.html'
    context_object_name = 'items_in_stock'

class ItemsInStockDetailView(DetailView):
    model = ItemsInStock
    template_name = 'inventory/items_in_stock_detail.html'
    context_object_name = 'items_in_stock'

class ItemsInStockCreateView(CreateView):
    model = ItemsInStock
    form_class = ItemsInStockForm
    template_name = 'inventory/items_in_stock_form.html'
    success_url = reverse_lazy('items-in-stock-list')

class ItemsInStockUpdateView(UpdateView):
    model = ItemsInStock
    form_class = ItemsInStockForm
    template_name = 'inventory/items_in_stock_form.html'
    success_url = reverse_lazy('items-in-stock-list')

class ItemsInStockDeleteView(DeleteView):
    model = ItemsInStock
    template_name = 'inventory/items_in_stock_confirm_delete.html'
    success_url = reverse_lazy('items-in-stock-list')


class VendorListView(ListView):
    model = Vendor
    template_name = 'inventory/vendor_list.html'
    context_object_name = 'vendors'

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'inventory/vendor_detail.html'
    context_object_name = 'vendor'

class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'inventory/vendor_form.html'
    success_url = reverse_lazy('vendor-list')

class VendorUpdateView(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'inventory/vendor_form.html'
    success_url = reverse_lazy('vendor-list')

class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'inventory/vendor_confirm_delete.html'
    success_url = reverse_lazy('vendor-list')

class PurchaseRecordListView(ListView):
    model = PurchaseRecord
    template_name = 'inventory/purchase_record_list.html'
    context_object_name = 'purchase_records'

class PurchaseRecordDetailView(DetailView):
    model = PurchaseRecord
    template_name = 'inventory/purchase_record_detail.html'
    context_object_name = 'purchase_record'

class PurchaseRecordCreateView(CreateView):
    model = PurchaseRecord
    form_class = PurchaseRecordForm
    template_name = 'inventory/purchase_record_form.html'
    success_url = reverse_lazy('purchase-record-list')

class PurchaseRecordUpdateView(UpdateView):
    model = PurchaseRecord
    form_class = PurchaseRecordForm
    template_name = 'inventory/purchase_record_form.html'
    success_url = reverse_lazy('purchase-record-list')

class PurchaseRecordDeleteView(DeleteView):
    model = PurchaseRecord
    template_name = 'inventory/purchase_record_confirm_delete.html'
    success_url = reverse_lazy('purchase-record-list')

class ReturnToVendorListView(ListView):
    model = ReturnToVendor
    template_name = 'inventory/return_to_vendor_list.html'
    context_object_name = 'returns_to_vendor'

class ReturnToVendorDetailView(DetailView):
    model = ReturnToVendor
    template_name = 'inventory/return_to_vendor_detail.html'
    context_object_name = 'return_to_vendor'

class ReturnToVendorCreateView(CreateView):
    model = ReturnToVendor
    form_class = ReturnToVendorForm
    template_name = 'inventory/return_to_vendor_form.html'
    success_url = reverse_lazy('return-to-vendor-list')

class ReturnToVendorUpdateView(UpdateView):
    model = ReturnToVendor
    form_class = ReturnToVendorForm
    template_name = 'inventory/return_to_vendor_form.html'
    success_url = reverse_lazy('return-to-vendor-list')

class ReturnToVendorDeleteView(DeleteView):
    model = ReturnToVendor
    template_name = 'inventory/return_to_vendor_confirm_delete.html'
    success_url = reverse_lazy('return-to-vendor-list')

class IssuanceListView(ListView):
    model = Issuance
    template_name = 'inventory/issuance_list.html'
    context_object_name = 'issuances'

class IssuanceDetailView(DetailView):
    model = Issuance
    template_name = 'inventory/issuance_detail.html'
    context_object_name = 'issuance'

class IssuanceCreateView(CreateView):
    model = Issuance
    form_class = IssuanceForm
    template_name = 'inventory/issuance_form.html'
    success_url = reverse_lazy('issuance-list')

class IssuanceUpdateView(UpdateView):
    model = Issuance
    form_class = IssuanceForm
    template_name = 'inventory/issuance_form.html'
    success_url = reverse_lazy('issuance-list')

class IssuanceDeleteView(DeleteView):
    model = Issuance
    template_name = 'inventory/issuance_confirm_delete.html'
    success_url = reverse_lazy('issuance-list')

class ReturnFromDepartmentListView(ListView):
    model = ReturnFromDepartment
    template_name = 'inventory/return_from_department_list.html'
    context_object_name = 'returns_from_department'

class ReturnFromDepartmentDetailView(DetailView):
    model = ReturnFromDepartment
    template_name = 'inventory/return_from_department_detail.html'
    context_object_name = 'return_from_department'

class ReturnFromDepartmentCreateView(CreateView):
    model = ReturnFromDepartment
    form_class = ReturnFromDepartmentForm
    template_name = 'inventory/return_from_department_form.html'
    success_url = reverse_lazy('return-from-department-list')

class ReturnFromDepartmentUpdateView(UpdateView):
    model = ReturnFromDepartment
    form_class = ReturnFromDepartmentForm
    template_name = 'inventory/return_from_department_form.html'
    success_url = reverse_lazy('return-from-department-list')

class ReturnFromDepartmentDeleteView(DeleteView):
    model = ReturnFromDepartment
    template_name = 'inventory/return_from_department_confirm_delete.html'
    success_url = reverse_lazy('return-from-department-list')

class CategoryListView(ListView):
    model = Category
    template_name = 'inventory/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_create.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_create.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'inventory/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')