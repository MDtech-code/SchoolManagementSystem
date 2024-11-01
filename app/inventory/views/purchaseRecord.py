from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.inventory.models import PurchaseRecord
from app.inventory.forms import PurchaseRecordForm
from django.urls import reverse_lazy

# PurchaseRecord View
class PurchaseRecordListView(ListView):
    model = PurchaseRecord
    template_name = 'inventory/purchase_record/purchase_record_list.html'
    context_object_name = 'purchase_records'
    def get_queryset(self):
        return PurchaseRecord.objects.select_related('stock_item', 'vendor', 'stock_item__item')
    
class PurchaseRecordDetailView(DetailView):
    model = PurchaseRecord
    template_name = 'inventory/purchase_record/purchase_record_detail.html'
    context_object_name = 'purchase_record'

class PurchaseRecordCreateView(CreateView):
    model = PurchaseRecord
    form_class = PurchaseRecordForm
    template_name = 'inventory/purchase_record/purchase_record_form.html'
    success_url = reverse_lazy('purchase-record-list')

class PurchaseRecordUpdateView(UpdateView):
    model = PurchaseRecord
    form_class = PurchaseRecordForm
    template_name = 'inventory/purchase_record/purchase_record_form.html'
    success_url = reverse_lazy('purchase-record-list')

class PurchaseRecordDeleteView(DeleteView):
    model = PurchaseRecord
    template_name = 'inventory/purchase_record/purchase_record_confirm_delete.html'
    success_url = reverse_lazy('purchase-record-list')
