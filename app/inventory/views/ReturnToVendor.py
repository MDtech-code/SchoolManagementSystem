from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.inventory.models import ReturnToVendor
from app.inventory.forms import ReturnToVendorForm
from django.urls import reverse_lazy

# ReturnToVender View
class ReturnToVendorListView(ListView):
    model = ReturnToVendor
    template_name = 'inventory/return_to_vendor/return_to_vendor_list.html'
    context_object_name = 'returns_to_vendor'

    def get_queryset(self):
     return ReturnToVendor.objects.select_related('stock_item', 'vendor', 'stock_item__item').distinct()


class ReturnToVendorDetailView(DetailView):
    model = ReturnToVendor
    template_name = 'inventory/return_to_vendor/return_to_vendor_detail.html'
    context_object_name = 'return_to_vendor'

class ReturnToVendorCreateView(CreateView):
    model = ReturnToVendor
    form_class = ReturnToVendorForm
    template_name = 'inventory/return_to_vendor/return_to_vendor_form.html'
    success_url = reverse_lazy('return-to-vendor-list')

class ReturnToVendorUpdateView(UpdateView):
    model = ReturnToVendor
    form_class = ReturnToVendorForm
    template_name = 'inventory/return_to_vendor/return_to_vendor_form.html'
    success_url = reverse_lazy('return-to-vendor-list')

class ReturnToVendorDeleteView(DeleteView):
    model = ReturnToVendor
    template_name = 'inventory/return_to_vendor/return_to_vendor_confirm_delete.html'
    success_url = reverse_lazy('return-to-vendor-list')
