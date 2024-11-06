# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from app.inventory.models import Vendor
# from app.inventory.forms import VendorForm
# from django.urls import reverse_lazy

# #Vender View
# class VendorListView(ListView):
#     model = Vendor
#     template_name = 'inventory/vendor/vendor_list.html'
#     context_object_name = 'vendors'

# class VendorDetailView(DetailView):
#     model = Vendor
#     template_name = 'inventory/vendor/vendor_detail.html'
#     context_object_name = 'vendor'

# class VendorCreateView(CreateView):
#     model = Vendor
#     form_class = VendorForm
#     template_name = 'inventory/vendor/vendor_form.html'
#     success_url = reverse_lazy('vendor-list')

# class VendorUpdateView(UpdateView):
#     model = Vendor
#     form_class = VendorForm
#     template_name = 'inventory/vendor/vendor_form.html'
#     success_url = reverse_lazy('vendor-list')

# class VendorDeleteView(DeleteView):
#     model = Vendor
#     template_name = 'inventory/vendor/vendor_confirm_delete.html'
#     success_url = reverse_lazy('vendor-list')
