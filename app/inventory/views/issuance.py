from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.inventory.models import Issuance
from app.inventory.forms import IssuanceForm
from django.urls import reverse_lazy

# Issuance View
class IssuanceListView(ListView):
    model = Issuance
    template_name = 'inventory/issuance/issuance_list.html'
    context_object_name = 'issuances'

    def get_queryset(self):
        return Issuance.objects.select_related('department', 'stock_item__item')

class IssuanceDetailView(DetailView):
    model = Issuance
    template_name = 'inventory/issuance/issuance_detail.html'
    context_object_name = 'issuance'

class IssuanceCreateView(CreateView):
    model = Issuance
    form_class = IssuanceForm
    template_name = 'inventory/issuance/issuance_form.html'
    success_url = reverse_lazy('issuance-list')

class IssuanceUpdateView(UpdateView):
    model = Issuance
    form_class = IssuanceForm
    template_name = 'inventory/issuance/issuance_form.html'
    success_url = reverse_lazy('issuance-list')

class IssuanceDeleteView(DeleteView):
    model = Issuance
    template_name = 'inventory/issuance/issuance_confirm_delete.html'
    success_url = reverse_lazy('issuance-list')